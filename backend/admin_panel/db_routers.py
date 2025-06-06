class SupabaseRouter:
    """
    A router to control all database operations on models in the console app (users, channels).
    """
    route_app_labels = {'console'}  # نام اپلیکیشن مربوط به users و channels

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'supabase'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'supabase'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'supabase'
        return db == 'default'
