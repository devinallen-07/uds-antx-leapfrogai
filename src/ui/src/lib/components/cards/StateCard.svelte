<script>
	import { Badge, Card, Alert } from 'flowbite-svelte';
	import { InfoCircleSolid } from 'flowbite-svelte-icons';
	export let states = [
		{
			stateOption: ''
		}
	];
</script>

<!-- <div class="bg-white py-24 sm:py-8"> -->
<div>
	<!-- <div class="mx-auto max-w-7xl px-6 lg:px-8"> -->
	<div>
		<!-- <div class="mx-auto max-w-2xl lg:mx-0">
			<span><h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">State</h2></span
			>
		</div> -->
		<!-- <div class="flex mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-x-0 gap-y-16 border-t border-gray-200 pt-10 sm:mt-8 sm:pt-8 lg:mx-0 lg:max-w-2xl lg:grid-cols-6"> -->
		<div class="flex m-4">
			{#each states as state}
				<Card color="primary">{state.stateOption}</Card>
			{/each}
		</div>
	</div>
</div>
