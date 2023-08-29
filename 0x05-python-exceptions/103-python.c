#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	    int i, size;
	        PyObject *item;

		    if (!PyList_Check(p))
			        {
					        printf("[ERROR] Invalid PyListObject\n");
						        return;
							    }

		        size = PyList_Size(p);
			    printf("[*] Python list info\n");
			        printf("[*] Size of the Python List = %d\n", size);
				    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

				        for (i = 0; i < size; i++)
						    {
							            item = PyList_GetItem(p, i);
								            printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
									        }
}

void print_python_bytes(PyObject *p)
{
	    int i, size;
	        unsigned char *data;

		    if (!PyBytes_Check(p))
			        {
					        printf("[ERROR] Invalid PyBytesObject\n");
						        return;
							    }

		        size = PyBytes_Size(p);
			    printf("[.] bytes object info\n");
			        printf("  [.] size: %d\n", size);
				    printf("  [.] trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

				        if (size > 10)
						        size = 10;

					    printf("  [.] first %d bytes:", size);
					        data = (unsigned char *)PyBytes_AsString(p);
						    for (i = 0; i < size; i++)
							            printf(" %02x", data[i]);
						        printf("\n");
}

void print_python_float(PyObject *p)
{
	    double value;

	        if (!PyFloat_Check(p))
			    {
				            printf("[ERROR] Invalid PyFloatObject\n");
					            return;
						        }

		    value = ((PyFloatObject *)p)->ob_fval;
		        printf("[.] float object info\n");
			    printf("  [.] value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

