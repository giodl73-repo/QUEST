PAPERS = glyph-campaign-spine \
         glyph-npc-arc \
         glyph-player-style \
         glyph-resource-exhaustion \
         glyph-rubric-amendment \
         glyph-rubric-instrument

.PHONY: all pdf clean

all: pdf

pdf:
	@for paper in $(PAPERS); do \
		echo "==> Building $$paper..."; \
		$(MAKE) -C publications/$$paper pdf || echo "WARN: $$paper failed"; \
	done

clean:
	@for paper in $(PAPERS); do \
		$(MAKE) -C publications/$$paper clean; \
	done
