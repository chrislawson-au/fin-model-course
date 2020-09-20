from typing import List

from lectures.dynamic_excel.main import get_dynamic_salary_excel_lecture
from lectures.dynamic_python.main import get_dynamic_salary_python_lecture
from lectures.intro.main import get_intro_lecture
from lectures.lab_exercises.main import get_lab_exercises_lecture
from lectures.model import LectureGroup
from lectures.projects.main import get_projects_lecture
from lectures.python_basics.main import get_python_basics_lecture
from lectures.start_python_excel.main import get_getting_started_with_python_and_excel_lecture
from lectures.visualization.main import get_visualization_lecture


def get_lecture_groups(include_labs: bool = True, include_projects: bool = True) -> List[LectureGroup]:
    lectures = [
        get_intro_lecture(),
        get_getting_started_with_python_and_excel_lecture(),
        get_dynamic_salary_excel_lecture(),
        get_python_basics_lecture(),
        get_dynamic_salary_python_lecture(),
        get_visualization_lecture(),
    ]

    if not include_labs and not include_projects:
        return lectures

    projects = [
        get_projects_lecture(),
    ]

    if not include_labs:
        return [*lectures, *projects]

    lab_exercises = [
        get_lab_exercises_lecture(),
    ]



    return [
        *lectures,
        *projects,
        *lab_exercises,
    ]