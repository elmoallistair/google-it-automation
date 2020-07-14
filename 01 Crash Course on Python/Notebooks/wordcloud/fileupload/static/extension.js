if (window.require) {
    window.require.config({
        map: {
            '*': {
                'fileupload': 'nbextensions/fileupload/widget',
                'jupyter-js-widgets': 'nbextensions/jupyter-js-widgets/extension'
            }
        }
    });
}
