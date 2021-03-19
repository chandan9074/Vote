from django.urls import path

from .views import (
    PrivatePollView,
    PublicPollView,
    PublicPollDetailsView,
    PrivatePollDetailsView,
    PublicPollOptionView,
    PrivatePollOptionView,
    UserPublicPollSerializerView,
    SpecificPublicPollOptionView,
    UserPrivatePollSerializerView,
    SpecificPrivatePollOptionView,
    PublicPollResultView,
    PrivatePollResultView,
    PrivatePollRequestView,
    PublicPollCountView,
    PublicPollOptionCountView,
    PrivatePollCountView,
    PrivatePollOptionCountView,
    PersonalPublicPollResultView,
    SinglePublicPollOptionView,
    UserDetailsView,
    PublicPollResultByUser,
    PersonalPrivatePollResultView,
    SinglePrivatePollOptionView,
    PrivatePollResultByUser,
)

urlpatterns = [
    path("private_poll_view/", PrivatePollView.as_view()),
    path("public_poll_view/", PublicPollView.as_view()),
    path("private_poll_details_view/<int:pk>/", PrivatePollDetailsView.as_view()),
    path("public_poll_details_view/<int:pk>/", PublicPollDetailsView.as_view()),
    path("private_poll_option_view/", PrivatePollOptionView.as_view()),
    path("public_poll_option_view/", PublicPollOptionView.as_view()),
    path("user_public_poll_view/<int:pk>/", UserPublicPollSerializerView.as_view()),
    path(
        "specific_public_poll_option_view/<int:pk>/",
        SpecificPublicPollOptionView.as_view(),
    ),
    path("user_private_poll_view/<int:pk>/", UserPrivatePollSerializerView.as_view()),
    path(
        "specific_private_poll_option_view/<int:pk>/",
        SpecificPrivatePollOptionView.as_view(),
    ),
    path("public_poll_result_view/", PublicPollResultView.as_view()),
    path("private_poll_result_view/", PrivatePollResultView.as_view()),
    path("private_poll_request_view/<str:pas>/", PrivatePollRequestView.as_view()),

    path("public_poll_count_view/<int:pk>/", PublicPollCountView.as_view()),

    path("public_poll_option_count_view/<int:pk>/", PublicPollOptionCountView.as_view()),

    path("private_poll_count_view/<int:pk>/", PrivatePollCountView.as_view()),

    path("private_poll_option_count_view/<int:pk>/", PrivatePollOptionCountView.as_view()),

    path("personal_public_poll_result_view/<int:pk>/", PersonalPublicPollResultView.as_view()),

    path("personal_private_poll_result_view/<int:pk>/", PersonalPrivatePollResultView.as_view()),

    path("single_public_poll_option_view/<int:pk>/", SinglePublicPollOptionView.as_view()),

    path("single_private_poll_option_view/<int:pk>/", SinglePrivatePollOptionView.as_view()),

    path("user_details_view/<int:pk>/", UserDetailsView.as_view()),

    path("public_poll_result_by_user/<int:pk>/", PublicPollResultByUser.as_view()),

    path("private_poll_result_by_user/<int:pk>/", PrivatePollResultByUser.as_view()),
]