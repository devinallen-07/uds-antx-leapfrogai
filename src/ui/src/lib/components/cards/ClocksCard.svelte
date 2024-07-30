<script>
	import { Badge } from 'flowbite-svelte';
	import { eventStore } from '../../../stores/stateStore';
</script>

<div class="m-4 flex flex-wrap justify-center text-lg dark:text-white">
		<p class="m-2 text-lg">Event Start</p>
		<Badge border><div>{$eventStore.metadata.eventStart}</div>
		</Badge>

		<p class="m-2 text-lg">Time to Next State</p>
		<Badge border><div>{$eventStore.metadata.timeToNextEvent}</div>
		</Badge>

		<p class="m-2 text-lg">Event Start</p>
		<Badge border><div>{$eventStore.metadata.runningClock}</div>
		</Badge>
</div>