from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'wl/index.html')

