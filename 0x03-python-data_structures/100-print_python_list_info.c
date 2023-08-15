#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

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

	size = PyList_Size(p);
	printf("[*] Size of the python list = %d\n", size);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(list_item)->tp_name);
	}
}
