from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.urls import include, path

from .views import (AddBoard, AddBoardAjax, AddCard, AddCardAjax,
                    AddCardMember, AddCheckList, AddComment, AddList,
                    AddListAjax, ArchiveCard, Attatchments, BoardArchive,
                    BoardContent, BoardRestore, CardArchives, ChangeCard,
                    ChecklistCheck, DeleteAttatchment, DeleteBoard, DeleteCard,
                    DeleteCheckList, DeleteList, EditBoard, EditBoardAjax,
                    EditCard, EditCardAjax, EditList, EditListAjax,
                    HomeRedirect, InviteMember, LinkInviteMember,
                    RemoveCardMember, RestoreCard, Search, SignUp, ViewBoards,
                    ViewCard)

urlpatterns = [
    path('', ViewBoards.as_view(), name="viewBoards"),
    path('board/new/', AddBoard.as_view(), name="addBoard"),
    path('board/<int:board_id>/edit/', EditBoard.as_view(), name="editBoard"),
    path('board/<int:board_id>/delete/', DeleteBoard.as_view(), name="deleteBoard"),
    path('board/<int:board_id>/archive/', BoardArchive.as_view(), name="archiveBoard"),
    path('board/<int:board_id>/restore/', BoardRestore.as_view(), name="restoreBoard"),
    path('board/<int:board_id>/', BoardContent.as_view(), name="boardContent"),
    path('board/<int:board_id>/list/new/', AddList.as_view(), name="addList"),
    path('board/<int:board_id>/<int:list_id>/edit/', EditList.as_view(), name="editList"),
    path('board/<int:board_id>/<int:list_id>/delete/', DeleteList.as_view(), name="deleteList"),
    path('board/<int:board_id>/<int:list_id>/add/', AddCard.as_view(), name="addCard"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/edit/', EditCard.as_view(), name="editCard"),
    path('board/<int:board_id>/<int:card_id>/delete/', DeleteCard.as_view(), name="deleteCard"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/archive/', ArchiveCard.as_view(), name="archiveCard"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/view/', ViewCard.as_view(), name="viewCard"),
    path('board/<int:board_id>/archives/', CardArchives.as_view(), name="cardArchives"),
    path('board/<int:board_id>/<int:card_id>/restore/', RestoreCard.as_view(), name="restoreArchivedCard"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/attatchment/', Attatchments.as_view(), name="cardAttatchment"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/<int:attchment_id>/delete/', DeleteAttatchment.as_view(), name="deleteAttatchment"),

    path('board/<int:board_id>/invite/', InviteMember.as_view(), name="inviteMember"),
    path('board/<int:board_id>/invite/ajax/', InviteMember.as_view(), name="inviteMemberAjax"),
    path('board/<int:board_id>/<uuid:invitation_id>/invite/', LinkInviteMember.as_view(), name="linkInviteMembers"),
    path('board/home/', HomeRedirect.as_view(), name="homeRedirect"),
    path('board/search/', Search.as_view(), name="search"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/<int:member_id>/', AddCardMember.as_view(), name="addCardMember"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/<int:member_id>/remove', RemoveCardMember.as_view(), name="removeCardMember"),


    path('accounts/signup/', SignUp.as_view(), name='signUp'),
    path('accounts/password_reset/', PasswordResetView.as_view(), name='passwordReset'),

    path('board/new/ajax/', AddBoardAjax.as_view(), name="addBoardAjax"),
    path('board/<int:board_id>/edit/ajax/', EditBoardAjax.as_view(), name="editBoardAjax"),
    path('board/<int:board_id>/list/new/ajax/', AddListAjax.as_view(), name="addListAjax"),
    path('board/<int:board_id>/<int:list_id>/edit/ajax/', EditListAjax.as_view(), name="editListAjax"),
    path('board/<int:board_id>/<int:list_id>/add/ajax/', AddCardAjax.as_view(), name="addCardAjax"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/edit/ajax/', EditCardAjax.as_view(), name="editCardAjax"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/edit/change/', ChangeCard.as_view(), name="changeCard"),

    path('board/<int:board_id>/<int:list_id>/<int:card_id>/checklist/add/', AddCheckList.as_view(), name="addChecklist"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/<int:cl_id>/cl/delete/', DeleteCheckList.as_view(), name="deleteChecklist"),
    path('board/<int:cl_id>/cl/check/', ChecklistCheck.as_view(), name="checklistCheck"),
    path('board/<int:board_id>/<int:list_id>/<int:card_id>/comment/add/', AddComment.as_view(), name="addComment"),
    
    
]
