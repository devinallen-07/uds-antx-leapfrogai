<script>
	import { Badge } from 'flowbite-svelte';
	export let testimonials = [
		{
			title1: '',
			title2: ''
		}
	];
</script>

<div class="m-4 flex flex-wrap justify-center text-lg">
	{#each testimonials as testimonial}
		<p class="m-2 text-lg dark:text-white">{testimonial.title1}</p>
		<Badge border>{testimonial.title2}</Badge>
	{/each}
</div>
