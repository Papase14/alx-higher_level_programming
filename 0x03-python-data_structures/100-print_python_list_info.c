#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	int x;
	PyObject *i;
	long int size = PyList_Size(p);
	long int alloc = ((PyListObject *)p)->allocated

	printf("[*] Size of the Python List = %ld/n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (x = 0; x < size; x++)
		i = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_Type(i)->tp_name)
}