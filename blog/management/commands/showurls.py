#!/usr/bin/env python
""" Script for creating custom commands for listing out urls """
from django.core.management.base import BaseCommand, CommandError
from django.urls import get_resolver


class Command(BaseCommand):

    help = "Listing out all the url in the project"

    def handle(self, *args, **options):
        self.stdout.write(
            get_resolver(),
            ending="\n"
        )
