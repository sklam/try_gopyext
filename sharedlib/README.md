Modify firsttry for shared library.

Anything that uses the runtime will break because it is not initialized.

TODO:

- Review runtime initialization in gopy:
    - https://github.com/qur/gopy/blob/ext/gccgo/ext.c
    - (a server plugin base on gopy) https://github.com/unbit/uwsgi/blob/master/plugins/gccgo/gccgo_plugin.c
    
