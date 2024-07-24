<script>
	import { Card } from 'flowbite-svelte';
	export let states = [
		{
			stateOption: ''
		}
	];
</script>

<div class="m-4 flex flex-wrap justify-center">
	{#each states as state}
		<div class="m-2 min-w-[200px] text-center">
			<Card color="primary">{state.stateOption}</Card>
		</div>
	{/each}
</div>
