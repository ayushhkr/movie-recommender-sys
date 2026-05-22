from dataclasses import asdict, dataclass, field


@dataclass
class RecommendationResult:
    query: str
    selected_title: str | None = None
    recommendations: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)
    error: str | None = None

    def to_dict(self):
        return asdict(self)


class RecommendationEngine:
    def __init__(self, movies, similarity):
        self.movies = movies.reset_index(drop=True).copy()
        self.similarity = similarity
        self.titles = self.movies["title"].fillna("").astype(str)
        self.normalized_titles = self.titles.str.strip().str.casefold().tolist()

    def recommend(self, movie_name, limit=5):
        query = str(movie_name or "").strip()
        if not query:
            return RecommendationResult(
                query="",
                error="Enter a movie title to get recommendations.",
            )

        normalized_query = query.casefold()
        exact_index = self._find_exact_index(normalized_query)
        if exact_index is not None:
            return self._build_result(query, exact_index, limit)

        partial_matches = [
            index
            for index, title in enumerate(self.normalized_titles)
            if normalized_query in title
        ]

        if not partial_matches:
            return RecommendationResult(
                query=query,
                error="No movie matched that title. Try one of the sample searches below.",
            )

        if len(partial_matches) > 1:
            suggestions = [self.movies.iloc[index].title for index in partial_matches[:5]]
            return RecommendationResult(
                query=query,
                suggestions=suggestions,
                error="Multiple matches found. Pick one of these exact titles.",
            )

        return self._build_result(query, partial_matches[0], limit)

    def _find_exact_index(self, normalized_query):
        for index, title in enumerate(self.normalized_titles):
            if title == normalized_query:
                return index
        return None

    def _build_result(self, query, movie_index, limit):
        distances = sorted(
            enumerate(self.similarity[movie_index]),
            reverse=True,
            key=lambda item: item[1],
        )

        recommendations = []
        seen_titles = {self.movies.iloc[movie_index].title}

        for candidate_index, _score in distances[1:]:
            title = self.movies.iloc[candidate_index].title
            if title in seen_titles:
                continue

            recommendations.append(title)
            seen_titles.add(title)

            if len(recommendations) == limit:
                break

        return RecommendationResult(
            query=query,
            selected_title=self.movies.iloc[movie_index].title,
            recommendations=recommendations,
        )
