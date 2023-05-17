#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - print basic list info
* @p: pointer to a pythonlistobject
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}

}
/**
* print_python_bytes - print python_object byte
* @p: pointer to a pyobject
*/
void print_python_bytes(PyObject *p)
{
    Py_ssize_t bytes;
    PyObject obj;
    int size;

    size = (PyVarObject *)p->ob_size;
    if (!p)
        printf("Error")
    /*Py_ssize_t_ob_refcnt */
    obj = ((PyListObject *)p);
    printf("[.] bytes object info");
    printf("size: %d", size);
    printf("first %d bytes", size);
}