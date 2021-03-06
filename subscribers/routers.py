# -*- coding: utf-8 -*-

class SubscriberRouter(object):
    """
    A router to control all database operations on models in the
    subscribers application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read subscribers models go to subscribers.
        """
        if model._meta.app_label == 'subscribers':
            return 'subscribers'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write subscribers models go to subscribers.
        """
        if model._meta.app_label == 'subscribers':
            return 'subscribers'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the subscribers app is involved.
        """
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        return None
