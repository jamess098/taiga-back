from unittest import mock

from django.core.urlresolvers import reverse

from taiga.projects.issues import services, models
from taiga.base.utils import json

from .. import factories as f

import pytest
pytestmark = pytest.mark.django_db


def test_get_issues_from_bulk():
    data = """
Issue #1
Issue #2
"""
    issues = services.get_issues_from_bulk(data)

    assert len(issues) == 2
    assert issues[0].subject == "Issue #1"
    assert issues[1].subject == "Issue #2"


@mock.patch("taiga.projects.issues.services.db")
def test_create_issues_in_bulk(db):
    data = """
Issue #1
Issue #2
"""
    issues = services.create_issues_in_bulk(data)

    db.save_in_bulk.assert_called_once_with(issues, None, None)


@mock.patch("taiga.projects.issues.services.db")
def test_update_issues_order_in_bulk(db):
    data = [(1, 1), (2, 2)]
    services.update_issues_order_in_bulk(data)

    db.update_in_bulk_with_ids.assert_called_once_with([1, 2], [{"order": 1}, {"order": 2}],
                                                       model=models.Issue)


def test_api_create_issues_in_bulk(client):
    project = f.create_project()

    url = reverse("issues-bulk-create")
    data = {"bulk_issues": "Issue #1\nIssue #2",
            "project_id": project.id}

    client.login(project.owner)
    response = client.json.post(url, json.to_json(data))

    assert response.status_code == 200, response.data


def test_api_filter_by_subject(client):
    f.create_issue()
    issue = f.create_issue(subject="some random subject")
    url = reverse("issues-list") + "?subject=some subject"

    client.login(issue.owner)
    response = client.get(url)
    number_of_issues = len(response.data)

    assert response.status_code == 200
    assert number_of_issues == 1, number_of_issues
