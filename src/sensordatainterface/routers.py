class SensorDataInterfaceRouter(object):
    """
    A router to control all database operations on models
    in the sensordatainterface application
    """

    def db_for_read(self, model, **hints):
        """
        Points all operations on sensordatainterface to 'odm2'
        """
        if model._meta.app_label == 'sensordatainterface':
            return 'odm2'
        return None

    def db_for_write(self, model, **hints):
        """
        Points all operations on sensordatainterface to 'odm2'
        """
        if model._meta.app_label == 'sensordatainterface':
            return 'odm2'
        return None
