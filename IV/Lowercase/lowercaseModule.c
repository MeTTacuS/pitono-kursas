#include <Python.h>

int areLowercase(char* str){
	for (int i = 0; str[i] != '\0'; i++) 
	{
		if (str[i] < 'a' || str[i] > 'z')
		{
			return 0;
		}
	}
	return 1;
}

static PyObject* lowercaseError;

static PyObject* py_lowercase(PyObject* self, PyObject* args)
{
	char* input;
	if(!PyArg_ParseTuple(args, "s", &input))
		return NULL;

	return Py_BuildValue("O", areLowercase(input) ? Py_True : Py_False);
}

static PyMethodDef lowercaseModuleMethods[]={
	{"AreLowercase", (PyCFunction)py_lowercase, METH_VARARGS, "Checks if the string is a lowercase word"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef lowercaseModule={
	PyModuleDef_HEAD_INIT,
	"LowercaseModule",
	"Lowercase Module",
	-1,
	lowercaseModuleMethods
};

PyMODINIT_FUNC PyInit_LowercaseModule(void)
{
	PyObject *mod =  PyModule_Create(&lowercaseModule);
	lowercaseError = PyErr_NewException("LowercaseModule.error", NULL, NULL);
	Py_INCREF(lowercaseError);
	PyModule_AddObject(mod, "error", lowercaseError);
	return mod;
}