from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "reader-dashboard/",
        views.reader_dashboard,
        name="reader_dashboard",
    ),

    path(
        "journalist-dashboard/",
        views.journalist_dashboard,
        name="journalist_dashboard",
    ),

    path(
        "editor-dashboard/",
        views.editor_dashboard,
        name="editor_dashboard",
    ),

    # Article workflow
    path(
        "articles/create/",
        views.create_article,
        name="create_article",
    ),

    path(
        "articles/<int:article_id>/edit/",
        views.edit_article,
        name="edit_article",
    ),

    path(
        "articles/<int:article_id>/delete/",
        views.delete_article,
        name="delete_article",
    ),

    path(
        "articles/pending/",
        views.pending_articles,
        name="pending_articles",
    ),

    path(
        "articles/<int:article_id>/approve/",
        views.approve_article,
        name="approve_article",
    ),
    path(
        "articles/<int:article_id>/approve/",
        views.approve_article,
        name="approve_article",
    ),

    # API endpoint
    path(
        "api/subscribed-articles/",
        views.SubscribedArticleAPIView.as_view(),
        name="subscribed_articles_api",
    ),

]
