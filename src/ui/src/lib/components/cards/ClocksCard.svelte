<script>
	import { Badge } from 'flowbite-svelte';
	import { eventStore } from '../../../stores/stateStore';
	export let testimonials = [
		{
			title1: '',
			title2: ''
		}
	];
</script>

<div class="m-4 flex flex-wrap justify-center text-lg dark:text-white">
	{#each testimonials as testimonial}
		<p class="m-2 text-lg">{testimonial.title1}</p>
		<Badge border><div>{$eventStore.metadata.eventStart}</div>
		</Badge>
	{/each}
</div>
