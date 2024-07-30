<script lang="ts">
	import { onMount, afterUpdate } from 'svelte';
	import { eventStore } from '../../../stores/stateStore';

	let contentContainer: HTMLElement | null = null;
	let userScrolling = false;
	let scrollTimeout: number | null = null;

	onMount(() => {
		scrollToBottom();
	});

	function scrollToBottom() {
		if (contentContainer && !userScrolling) {
			contentContainer.scrollTop = contentContainer.scrollHeight;
		}
	}

	function handleScroll() {
		userScrolling = true;
		if (scrollTimeout) {
			clearTimeout(scrollTimeout);
		}
		scrollTimeout = setTimeout(() => {
			userScrolling = false;
		}, 1000) as unknown as number; // 1 second delay
	}

	$: transcriptions = $eventStore.transcription?.speechToText || [];

	$: if (transcriptions) {
		afterUpdate(() => {
			scrollToBottom();
		});
	}
</script>

<div
	bind:this={contentContainer}
	on:scroll={handleScroll}
	class="mx-auto h-48 overflow-auto dark:[color-scheme:dark]"
>
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
