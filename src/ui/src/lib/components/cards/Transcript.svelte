<script lang="ts">
	import { onMount, afterUpdate } from 'svelte';
	import { eventStore } from '../../../stores/stateStore';

	let contentContainer: HTMLElement | null = null;
	let userScrolling = false;
	let scrollTimeout: number | null = null;
	let firstTimestamp: number | null = null;

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

	function parseTimestamp(timestamp: string): number {
		const parts = timestamp.split(/[- :T]/);
		return new Date(
			parseInt(parts[0]),
			parseInt(parts[1]) - 1,
			parseInt(parts[2]),
			parseInt(parts[3]),
			parseInt(parts[4]),
			parseInt(parts[5])
		).getTime();
	}

	function formatTime(date: Date): string {
		return date.toTimeString().split(' ')[0];
	}

	function formatDelta(deltaMs: number): string {
		const deltaHours = Math.floor(deltaMs / (1000 * 60 * 60));
		const deltaMinutes = Math.floor((deltaMs % (1000 * 60 * 60)) / (1000 * 60));
		return `+${deltaHours.toString().padStart(2, '0')}:${deltaMinutes.toString().padStart(2, '0')}`;
	}

	function processTimestamp(
		item: string,
		index: number
	): { formattedTime: string; content: string } {
		const [timestamp, ...contentParts] = item.split(' ');
		const content = contentParts.join(' ');

		try {
			const currentTime = parseTimestamp(timestamp);
			const date = new Date(currentTime);

			if (firstTimestamp === null) {
				firstTimestamp = currentTime;
			}

			const deltaMs = currentTime - firstTimestamp;
			const delta = formatDelta(deltaMs);
			const time = formatTime(date);

			const formattedTime = `${index + 1} ${time} (${delta})`;

			return { formattedTime, content };
		} catch (error) {
			console.error('Error processing timestamp:', error);
			return { formattedTime: `${index + 1} N/A`, content: item };
		}
	}

	$: transcriptions = $eventStore.transcription?.speechToText || [];

	$: if (transcriptions) {
		firstTimestamp = null; // Reset first timestamp when transcriptions change
		afterUpdate(() => {
			scrollToBottom();
		});
	}
</script>

<div
	bind:this={contentContainer}
	on:scroll={handleScroll}
	class="mx-auto h-96 overflow-auto dark:[color-scheme:dark]"
>
	<ul class="custom-ul rounded-lg p-4 text-white">
		{#each transcriptions as item, index}
			{@const { formattedTime, content } = processTimestamp(item, index)}
			<li class="custom-li">
				<span class="timestamp">{formattedTime}</span>
				<span class="content">{content}</span>
			</li>
		{/each}
	</ul>
</div>

<style>
	:global(.accordion-content) {
		padding: 0 !important;
	}

	.custom-ul {
		list-style-type: none;
		padding-left: 0;
		margin: 0;
	}

	.custom-li {
		margin-bottom: 4px;
	}

	.timestamp {
		font-weight: bold;
		margin-right: 8px;
		white-space: nowrap;
	}

	.content {
		word-break: break-word;
	}
</style>
