#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - function prints info on python list
 * @p: the python list object
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	int size;
	int allocated, i;
	PyObject *list_item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(list_item)->tp_name);
	}
}
