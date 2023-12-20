

interface BaseMessage {
  author_id: string
  parent_id?: string
  created_date: Date
  mod_date?: Date
  media_ids?: string[]
}
interface PostContent{
  title: string
  body: string
  sections?: PostContent[]
}
export interface Message extends BaseMessage{
  content: string
  recipient_id?: string
}
export interface Post extends BaseMessage {
  content: PostContent
}
