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
	listint_t *trav1 = *head, *trav2 = *head;
	int counter = 0, i, j, num;

	if (!*head)
		return (1);

	/*Calculate length of linked-list*/
	while (trav1)
	{
		counter++;
		trav1 = trav1->next;
	}

	/* Reusing trav1 */
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

	return (1);
}
