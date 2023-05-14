#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t length, i;
	/* to iteraate*/
	length = PyList_Size(list);
	for (i = 0; i < length; i++)
	{
		printf("index %d:  %s\n", i, Py_Type(Pylist_GetItem(p, i)->tp_name);
	}
	/*once we get size or length of the list we can traverse it*/
}
