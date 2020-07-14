from .widget import FileUploadWidget  # noqa


def _jupyter_nbextension_paths():
    return [dict(
        section='notebook',
        src='static',
        dest='fileupload',
        require='fileupload/extension')]
