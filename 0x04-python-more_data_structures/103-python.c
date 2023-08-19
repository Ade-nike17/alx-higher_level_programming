#include <Python.h>
#include <stdio.h>
#include <string.h>


/**
 * print_python_bytes - function prints info on python bybytes
 * @p: the python list object
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	int size, count, i;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	count = size >= 10 ? 10 : size + 1;

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %d bytes: ", count);
	         
	for (i = 0; i < count - 1; i++)
	{
		printf("%02x ", (unsigned char)bytes_obj->ob_sval[i]);
	}
	printf("%02x\n", bytes_obj->ob_sval[i]);
}



/**
 * print_python_list - function prints info on python list
 * @p: the python list object
 * Return: nothing
 */

void print_python_list(PyObject *p)
{
	int size;
	int i;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	size = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}
