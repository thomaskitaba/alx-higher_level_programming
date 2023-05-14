#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int length, i, allocated;
	PyObject *item;

	/* to iterate*/
	length = Py_SIZE(p);
	/* cast to PYlistobject pointer*/
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d", length);
	printf("[*] Allocated = %d", allocated);

	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
	/*once we get size or length of the list we can traverse it*/
}
