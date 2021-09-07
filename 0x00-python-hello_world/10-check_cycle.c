#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: linked list
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{

	listint_t *current = list;
	listint_t *check = list;

	if (list == NULL)
		return (0);

	while (current && current->next)
	{
		check = check->next;
		current = current->next->next;

		if (check == current)
			return (1);
	}
	return (0);
}
