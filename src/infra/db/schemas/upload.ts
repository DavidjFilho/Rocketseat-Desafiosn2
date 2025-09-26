import { pgTable, timestamp, varchar } from 'drizzle-orm/pg-core'
import { uuidv7 } from 'uuidv7'

export const uploads = pgTable('uploads', {
  id: varchar('id')
    .primaryKey()
    .notNull()
    .$defaultFn(() => uuidv7()),
  name: varchar('name').notNull(),
  remoteKey: varchar('remote_key').notNull().unique(),
  remoteUrl: varchar('remote_url').notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
})

// auto increment / uuid
