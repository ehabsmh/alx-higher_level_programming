#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is palindrome or not
 * @head: the head of Linked list
 * Return: 1 if palindrome OTHERWISE 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *traverse = *head;
	int len = 0, i, j;
	int *arr;

	if (!*head)
		return (1);

	while (traverse)
	{
		len++;
		traverse = traverse->next;
	}

	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);

	traverse = *head;

	for (i = 0; i < len; i++)
	{
		if (traverse)
		{
			arr[i] = traverse->n;
			traverse = traverse->next;
		}
	}

	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
