from django.shortcuts import render, get_object_or_404
from ..models import Question

import logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'wl/index.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'wl/question_detail.html', context)
