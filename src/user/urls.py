from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views.otp import OTPSignupView, OTPVerificationAPIView
from user.views.passport import PassportVerificationViewSet 


router = DefaultRouter()
router.register('passport-verification', PassportVerificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('otp/', OTPSignupView.as_view(), name='otp_signup'),
    path('otp/verification/', OTPVerificationAPIView.as_view(), name='otp_verification'),
    
]
