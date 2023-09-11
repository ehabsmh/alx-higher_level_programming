#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindrome or not
 * @head: the head of Linked list
 * Return: 1 if palindrome OTHERWISE 0
*/

/*
int is_palindrome(listint_t **head)
{
	listint_t *trav1 = *head, *trav2 = *head;
	int counter = 0, i, j, num;

	if (!*head)
		return (1);

	while (trav1)
	{
		counter++;
		trav1 = trav1->next;
	}

	trav1 = *head;

	for (i = 0; i < counter; i++)
	{
		if (trav1)
			num = trav1->n;

		for (j = counter - 1; j > i; j--)
			if (trav2)
				trav2 = trav2->next;

		if (trav2 && num != trav2->n)
			return (0);

		trav1 = trav1->next;
		trav2 = *head;
	}

	trav2 = NULL;
	return (1);
}
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
		arr[i] = traverse->n;
		traverse = traverse->next;
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
