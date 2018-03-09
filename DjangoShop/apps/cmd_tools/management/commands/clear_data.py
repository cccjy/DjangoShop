import os
import sys
import json

from django.core.management.base import BaseCommand

from goods.models import Goods, GoodsCategory, GoodsImage


def clear():
    pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear()
