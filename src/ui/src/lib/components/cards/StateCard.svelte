<script>
	import { Card } from 'flowbite-svelte';
	export let list = [{ state: '', isCurrent: true }];
</script>

<div class="m-4 flex flex-wrap justify-center dark:text-white">
	{#each list as { state, isCurrent }}
		<div class="m-2 min-w-[200px] text-center {isCurrent ? 'glow-border' : 'glow-border-inactive'} border-transparent rounded-lg">
			<Card color="primary" class="dark:bg-gray-700">{state}</Card>
		</div>
	{/each}
</div>

<style>
	@keyframes glow {
	  0% {
		box-shadow: 0 0 5px #2494d1, 0 0 10px #2494d1, 0 0 15px #2494d1, 0 0 20px #2494d1;
	  }
	  50% {
		box-shadow: 0 0 10px #2494d1, 0 0 20px #2494d1, 0 0 30px #2494d1, 0 0 40px #2494d1;
	  }
	  100% {
		box-shadow: 0 0 5px #2494d1, 0 0 10px #2494d1, 0 0 15px #2494d1, 0 0 20px #2494d1;
	  }
	}

	.glow-border {
	  animation: glow 2s infinite;
	}

	.glow-border-inactive {
	  animation: none;
	}
  </style>