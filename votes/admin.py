from django.contrib import admin
from votes.models import *


admin.site.register(PrivatePoll)
admin.site.register(PublicPoll)
admin.site.register(PrivatePollOption)
admin.site.register(PublicPollOption)
admin.site.register(PublicPollResult)
admin.site.register(PrivatePollResult)