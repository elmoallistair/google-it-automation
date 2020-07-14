import base64
import ipywidgets
import traitlets


class FileUploadWidget(ipywidgets.DOMWidget):
    '''File Upload Widget.
    This widget provides file upload using `FileReader`.
    '''
    _view_name = traitlets.Unicode('FileUploadView').tag(sync=True)
    _view_module = traitlets.Unicode('fileupload').tag(sync=True)

    label = traitlets.Unicode(help='Label on button.').tag(sync=True)
    filename = traitlets.Unicode(help='Filename of `data`.').tag(sync=True)
    data_base64 = traitlets.Unicode(help='File content, base64 encoded.'
                                    ).tag(sync=True)
    data = traitlets.Bytes(help='File content.')

    def __init__(self, label="Browse", *args, **kwargs):
        super(FileUploadWidget, self).__init__(*args, **kwargs)
        self._dom_classes += ('widget_item', 'btn-group')
        self.label = label

    def _data_base64_changed(self, *args):
        self.data = base64.b64decode(self.data_base64.split(',', 1)[1])
