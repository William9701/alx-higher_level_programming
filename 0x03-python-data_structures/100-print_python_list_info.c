#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = PyList_Size(p);
	if (size == -1)
	{
		printf("[*] Error: Invalid Python list.\n");
		return;
	}
	printf("[*] Size of the Python List: %ld\n", size);
	printf("[*] Allocated Memory: %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		if (obj != NULL)
		{
			printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		}
		else
		{
			printf("Element %ld: [Error retrieving object]\n", i);
		}
	}
}

