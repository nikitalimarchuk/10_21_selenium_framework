from datetime import datetime
from typing import List

from core.domain.result import Result
from core.infrastructure.repositories.base_repository import BaseRepository
from core.infrastructure.models import TestResult


class TestResultRepository(BaseRepository):
    def save_all(self, test_results: List[Result]) -> None:
        report = []

        for test_result in test_results:
            report.append(
                TestResult(**test_result.to_dict())
            )

        self._session.add_all(report)
        self._session.commit()
