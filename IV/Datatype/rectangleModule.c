#include <Python.h>
#include "structmember.h"
#include <stdio.h>

typedef struct{
  PyObject_HEAD
  float length;
  float width;
} Rectangle;

static PyObject* rectangleError;

static void Rectangle_dealloc(Rectangle* self){
	Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject * Rectangle_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Rectangle *self;

    self = (Rectangle *)type->tp_alloc(type, 0);
    if (self != NULL) {
      self->length = 1;
      self->width = 1;
    }

    return (PyObject *)self;
}

static int Rectangle_init(Rectangle *self, PyObject *args, PyObject *kwds)
{
	float tempA, tempB;
	if (!PyArg_ParseTuple(args, "ff", &tempA, &tempB))
    return -1;
	
	if(tempA <= 0 || tempB <= 0){
		PyErr_SetString(rectangleError, "Sides must have a positive value");
		return -1;
	}

	self->length=tempA;
	self->width=tempB;
	
  return 0;
}

static PyObject * Rectangle_perimeter(Rectangle* self)
{
	char str[10];
	sprintf(str, "%.3f", self->width + self->width + self->length + self->length);
	return Py_BuildValue("s", str);
}

static PyObject * Rectangle_area(Rectangle* self)
{
	char str[10];
	sprintf(str, "%.3f", self->length * self-> width);
	return Py_BuildValue("s", str);
}

static PyObject* Rectangle_str(Rectangle* self){
	char str1[10];
	char str2[10];
	sprintf(str1, "%.2f", self->length);
	sprintf(str2, "%.2f", self->width);
	return PyUnicode_FromFormat("length = %s, width = %s", str1, str2);
}

static PyMemberDef Rectangle_members[] = {
    {"a", T_FLOAT, offsetof(Rectangle, length), 0, "Rectangle length"},
    {"b", T_FLOAT, offsetof(Rectangle, width), 0, "Rectangle width"},
    {NULL}  
};

static PyMethodDef Rectangle_methods[] = {
    {"perimeter", (PyCFunction)Rectangle_perimeter, METH_NOARGS, "Returns the perimeter of a rectangle"},
	  {"area", (PyCFunction)Rectangle_area, METH_NOARGS, "Returns area of a rectangle"},
    {NULL}  
};

static PyTypeObject RectangleType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "rectangle.Rectangle",             /* tp_name */
    sizeof(Rectangle),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Rectangle_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    (reprfunc)Rectangle_str,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "This is a rectangle",        /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Rectangle_methods,             /* tp_methods */
    Rectangle_members,             /* tp_members */
    0,           				/* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Rectangle_init,      /* tp_init */
    0,                         /* tp_alloc */
    Rectangle_new,                 /* tp_new */
};

static struct PyModuleDef rectangleModule ={
  PyModuleDef_HEAD_INIT, 
  "RectangleModule",
  "Rectangle type",
  -1,
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_Rectangle (void){
  PyObject* m;
  if (PyType_Ready(&RectangleType)< 0) 
    return NULL;
  m = PyModule_Create(&rectangleModule);
  if (m == NULL)
    return NULL;
  Py_INCREF(&RectangleType);
  PyModule_AddObject(m, "Rectangle", (PyObject*)&RectangleType);
  
  rectangleError = PyErr_NewException("rectangle.error", NULL, NULL);
  Py_INCREF(rectangleError);
  PyModule_AddObject(m, "error", rectangleError);
  
  return m; 
}


