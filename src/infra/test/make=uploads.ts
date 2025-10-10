import { db } from '../db'
import { schema } from '../db/schemas'
import { fakerPT_BR as faker } from '@faker-js/faker'

export async function makeUpload() {
  const result = await db
    .insert(schema.uploads)
    .values({
      name: 'teste.jpg',
      remoteKey: 'teste.jpg',
      remoteUrl: faker.internet.url(),
    })
    .returning()

  return result[0]
}
