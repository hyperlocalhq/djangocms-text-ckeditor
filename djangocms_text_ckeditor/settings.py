from django.conf import settings

#See http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.config.html for all settings

CKEDITOR_SETTINGS = getattr(settings, 'CKEDITOR_SETTINGS', {
    'language': '{{ language }}',
    'toolbar': 'Basic',
    'skin': 'kama',
    'toolbarCanCollapse': False,
})

TEXT_SAVE_IMAGE_FUNCTION = getattr(settings, 'TEXT_SAVE_IMAGE_FUNCTION', 'djangocms_text_ckeditor.picture_save.create_picture_plugin')



