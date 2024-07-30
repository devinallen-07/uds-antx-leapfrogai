<script lang="ts">
	import { onMount } from 'svelte';
	import { eventStore } from '../../../stores/stateStore';

	let contentContainer: HTMLElement | null = null;

	onMount(() => {
		if (contentContainer) {
			contentContainer.scrollTop = contentContainer.scrollHeight;
		}
	});

    $: transcriptions = $eventStore.transcription?.speechToText || [];
</script>

<div bind:this={contentContainer} class="mx-auto h-48 overflow-auto dark:[color-scheme:dark]">
	<ol class="custom-ol rounded-lg p-4 text-white">
		{#each transcriptions as item}
			<li>
				<div class="custom-li-content">{item}</div>
			</li>
		{/each}
	</ol>
</div>

<style>
	:global(.accordion-content) {
		padding: 0 !important;
	}

	.custom-ol {
		list-style-type: none;
		padding-left: 0;
		margin: 0;
	}
	.custom-ol li {
		counter-increment: custom-counter;
	}
	.custom-ol li::before {
		content: counter(custom-counter);
		margin-right: 6px;
	}
	.custom-li-content {
		display: inline-block;
		max-width: calc(100% - 30px); /* Adjusts max width to prevent overlap with the counter */
		vertical-align: top; /* Aligns content at the top */
	}
</style>
