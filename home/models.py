from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class DefaultPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class GigBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    date = blocks.DateBlock()
    link = blocks.URLBlock(required=False)
    description = blocks.RichTextBlock(required=False)
    private = blocks.BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'user'

    def __str__(self):
        return "{} - {}".format(self.date, self.title)


class GigsPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('gig', GigBlock()),
    ])
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
