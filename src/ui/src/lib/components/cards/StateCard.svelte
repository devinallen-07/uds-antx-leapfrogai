<script>
	import { Card } from 'flowbite-svelte';
	export let list = [''];
</script>

<div class="m-4 flex flex-wrap justify-center dark:text-white">
	{#each list as state}
		<div class="m-2 min-w-[200px] text-center">
			<Card color="primary" class="dark:bg-gray-700">{state}</Card>
		</div>
	{/each}
</div>
