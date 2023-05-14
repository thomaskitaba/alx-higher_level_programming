#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int length, alloc, i;
	PyObject *item;

	length = Py_length(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] length of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < length; i++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}

}
