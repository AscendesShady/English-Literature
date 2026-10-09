"""Story-specific additional beats and a spoken narration pass for the older library.

The new beats deepen decisions and consequences; they do not fabricate dialogue.
Existing scene keys support reading-position migration across content editions.
"""
EXTRA = {
'the-odyssey': '''1|The son must grow up|Telemachus cannot wait forever for his father! His search for news makes the silent household part of the voyage too.|ship
3|The name becomes a weapon|Nobody saved Odysseus inside the cave—but his real name exposes him outside it! Watch clever victory turn into dangerous pride.|mask
4|The warning meets appetite|His companions have been warned about the sacred cattle. Hunger presses against obedience! Their choice makes the promised journey home impossible for them.|apple
5|The listener offers a ship|A good audience does more than applaud! Phaeacian hospitality gives the exhausted wanderer the means to leave the story's telling and reach home.|ship
6|The household must recognise him|Ithaca is near, but recognition is still dangerous! Odysseus needs loyal help and a careful plan before a returned stranger can become its king.|bow''',
'antigone': '''1|The sister sees the danger|Ismene fears what defiance will cost. Can love take two different forms? Her caution makes Antigone's solitude sharper, not less real.|heart
2|The deed cannot be hidden by denial|Caught before Creon, Antigone owns the burial. What a direct challenge! The king must now answer conviction rather than a convenient excuse.|crown
3|Authority grows afraid of listening|Creon treats resistance as a threat to rule. Notice the trap! Protecting authority becomes the very behaviour that puts his household at risk.|chains
4|A son risks disagreement|Haemon speaks as someone who loves his father and Antigone. Can Creon hear loyalty inside criticism? His refusal drives father and son apart.|heart
6|The rescuer is finally on the road|Creon moves to reverse the sentence. At last—but how much time has passed? Good intentions must now catch consequences already in motion.|road''',
'beowulf': '''1|The stranger asks for the fight|Beowulf offers help where terror has silenced the hall. His confidence matters! But reputation will soon have to become action before witnesses.|sword
2|The boast meets a remembering rival|Unferth questions Beowulf's earlier adventures. Can the newcomer defend his name? The feast hall becomes a contest of stories before the bodily contest begins.|hall
3|The trophy cannot end the danger|Grendel's arm hangs in victory, but someone else grieves him. Beware the easy ending! A defeated enemy can leave a new motive behind.|grave
4|The hero enters another household|Below the water Beowulf faces the mother's strength. The celebrant is now the intruder! Another battle tests what the earlier victory could not settle.|cave
6|The young warrior remembers his debt|Wiglaf stays when others flee. What does allegiance mean without danger? His remembered obligation becomes visible at the moment loyalty costs something.|sword''',
'the-canterbury-tales': '''1|A reward gives the voices a frame|The Host offers a supper for the best storyteller. Now the journey has a game! Social companions become performers competing for an audience.|hall
2|The storyteller can be judged too|A pilgrim's tale may sound different beside the pilgrim's behaviour. Listen twice! Chaucer makes the speaker's self-presentation part of what the story means.|mirror
3|The interrupted order stays broken|The Miller refuses to wait politely. There goes the tidy hierarchy! The contest lets a lower-status voice overturn the expected sequence of dignified speakers.|road
4|Experience answers the authorities|The Wife of Bath cites her own marriages against inherited judgements. Who gets to explain women's lives? Her prologue turns personal experience into a contested authority.|book
6|The sermon catches its speaker|The Pardoner exposes his own greed while condemning it. What a contradiction! A powerful moral tale can come from someone who violates its lesson.|coins''',
'the-spanish-tragedy': '''1|The war leaves a private rivalry|Victory does not clear the stage! Balthazar's desire and Lorenzo's ambition draw the survivors into another struggle, now around love and household power.|crown
2|The garden holds a murdered son|Hieronimo finds Horatio's body where love had seemed possible. A father's world breaks! Public honour cannot protect the intimate life he most values.|grave
3|The letter offers dangerous knowledge|Bel-imperia's message points toward the killers. Can Hieronimo trust and use it? Learning the truth is only the beginning of obtaining justice.|letter
4|The appeal reaches a closed system|Powerful enemies can frustrate his appeals. Where can a grieving father turn? The failure of ordinary justice makes the imagined revenge increasingly attractive.|chains
6|The actors do not know the whole play|The court expects entertainment, but Hieronimo has another purpose. Watch the stage! A represented death is about to become a real consequence.|stage''',
'the-faerie-queene': '''1|A guide can appear virtuous|Redcrosse needs more than courage to choose the right companion. How easy deception becomes when it borrows the appearance of wisdom and goodness!|mask
2|The false lady wins attention|Duessa's attractive surface competes with Una's truth. Look carefully! The knight's moral journey includes learning that beauty and trustworthy guidance are different things.|mirror
3|Despair makes a persuasive argument|Redcrosse meets despair that can reason against hope. A sword is not enough! He needs help to resist a voice working inside judgement itself.|grave
4|Holiness must be restored before battle|Una guides him toward recovery and instruction. Notice the pause! Moral preparation belongs to heroism as much as the spectacular fight against the dragon.|temple
6|Different virtues face different temptations|Guyon and Britomart cannot simply repeat Redcrosse's trial. Temperance and chastity have their own tests! The allegory becomes a family of moral journeys.|book''',
'doctor-faustus': '''1|The scholar wants an unlimited door|Ordinary learning no longer satisfies Faustus. What would enough knowledge look like? His ambition begins by refusing the limits that give human choices their shape.|book
2|The warning comes from the servant|Mephistopheles describes his own suffering. Faustus hears—and still bargains! The danger is spoken before the agreement, making his refusal to listen part of the tragedy.|fire
3|The signature meets resistance|His blood congeals as he signs. Even the body seems to interrupt the bargain! Faustus presses on toward a freedom already written as servitude.|contract
4|The great promise becomes small tricks|What happened to boundless achievement? Spectacles and pranks consume the years, exposing the distance between the scholar's dream and the power he actually uses.|mask
6|The last hour cannot be stretched|The clock keeps moving while Faustus imagines escape. How terrible the limit now feels! A lifetime of postponement gathers into minutes he cannot command.|clock''',
'othello': '''1|The marriage already needs defence|Othello and Desdemona have chosen each other against opposition. Their courage deserves attention! Iago will attack a trust that has already faced public pressure.|heart
2|The helpful voice prepares the wound|Iago offers the manner of loyal service. Who suspects the hand that seems to help? His outward concern gives poison a safe route into confidence.|mask
3|A ruined night creates an opening|Cassio's drunken fight costs him his post. Desdemona's help seems generous! Iago turns that attempt to repair one injury into apparent evidence of another.|hall
4|The token leaves its first meaning|The handkerchief once belonged to love and remembrance. Now it travels through other hands! An object can keep its appearance while its alleged meaning changes.|cloth
6|The witness will not remain silent|Emilia understands too late how the token was used. Her testimony threatens Iago! Truth finally speaks clearly after suspicion has already been allowed to kill.|letter''',
'macbeth': '''1|Two futures stand beside one another|The witches promise Macbeth kingship and Banquo a royal line. Listen for the difference! A desired future can plant rivalry before either man has acted.|stars
2|The letter carries temptation home|Lady Macbeth reads the prophecy and sees a route to power. The castle changes mood! A private marriage becomes the place where ambition begins planning violence.|letter
3|The guest is also their king|Duncan comes under their protection. What a betrayal the plan requires! Hospitality and allegiance must be broken before Macbeth can take the crown.|castle
4|The crown makes another man frightening|Banquo knows enough to trouble Macbeth. Victory has not brought safety! The new king's fear turns the prophecy's second promise into another motive for murder.|crown
6|The queen cannot wash away memory|Lady Macbeth's sleepwalking reveals a mind burdened by the deed. Water cannot settle this wound! What seemed a manageable stain has become an inward haunting.|bed''',
'the-tempest': '''1|The storm has a hidden director|Prospero commands the tempest while preserving the passengers' lives. The opening terror is staged! We begin by watching power control what others believe has happened.|ship
2|A father controls the telling|Prospero explains their exile to Miranda. His account gives her a history! But he also decides when knowledge arrives and what shape it takes.|book
3|Love enters a planned encounter|Miranda and Ferdinand meet within Prospero's design. Their feeling is real! The uncertainty concerns how freely affection develops inside a world organised by someone else's will.|heart
4|The island contains competing claims|Caliban remembers the island as his own inheritance. Hear the grievance! Prospero's authority is not the only account of belonging that this place contains.|stone
6|The magic must end with the judgement|Prospero can punish his enemies, but chooses release. What makes that decision complete? Giving up his staff means surrendering the means of endless control as well.|book''',
'paradise-lost': '''1|The rebel makes defeat sound heroic|Satan's rhetoric offers comrades a grand identity after loss. Hear its appeal! Eloquence can make a destructive purpose feel like dignity recovered.|fire
2|The council divides imagined remedies|The fallen angels debate their response. What can wounded pride invent? Revenge against another creation becomes a way to refuse responsibility for their own rebellion.|hall
3|The garden contains a choice|Adam and Eve receive freedom with a prohibition. Obedience is not automatic! A meaningful relationship to their creator includes the possibility of acting against the command.|apple
4|The serpent separates language from intention|Temptation argues that the forbidden act will bring improvement. How familiar that promise sounds! The offered benefit conceals the speaker's wish to damage the hearer.|mask
6|Blame cannot rebuild the garden|Adam and Eve accuse each other after the fall. Their quarrel deepens loss! Reconciliation requires accepting responsibility before they can face a future beyond Eden.|heart''',
'to-his-coy-mistress': '''1|The impossible beginning sounds generous|The speaker imagines lavish time for patient courtship. Listen to the condition! Its generosity belongs to a world he will immediately declare impossible.|garden
2|The praise measures a fantasy|Centuries of admiration enlarge the imagined devotion. What is this delay preparing? The poem's first movement builds the patience its next movement takes away.|clock
3|The body enters the argument|Mortality becomes the speaker's pressure on the addressee. His urgency is persuasive! But her silence prevents us from claiming that she accepts the invitation.|grave
4|The grave becomes a rhetorical opponent|The speaker turns death into the reason for present intimacy. Notice who sets the alternatives! The argument presents urgency through his desired outcome.|chains
5|The final energy remains a proposal|The lovers are imagined acting together, not shown agreeing in separate voices. Keep that distinction! A brilliant argument cannot supply the silent listener's consent.|heart
6|Remember the three turns|If there were time; but there is not; therefore act! The logical pattern makes the poem memorable while leaving its persuasive pressure open to examination.|book''',
'the-way-of-the-world': '''1|The inheritance sits between the lovers|Mirabell and Millamant cannot plan only around affection. Money has a gatekeeper! Their romance moves through the arrangements that make desire materially possible.|coins
2|An older woman's wish becomes a lever|Lady Wishfort's vulnerability to flattery gives the scheme its opening. What can apparent admiration hide? The comedy makes courtship another instrument of control.|mask
3|A servant needs a borrowed rank|Waitwell's disguised identity supplies the planned deception. Watch names and costumes! Social authority can be performed convincingly enough to move other people's choices.|crown
4|The bride insists on private space|Millamant's conditions protect habits and independence within marriage. How lively that negotiation is! Love must agree to leave room for the person it hopes to possess.|contract
6|A document defeats the blackmailer|The final protection depends upon a legal arrangement already made. Wit needs paperwork! Private desire survives because someone has anticipated the material use of power.|letter''',
'the-rape-of-the-lock': '''1|A morning looks like a ceremony|Belinda prepares herself with cosmetics and attention. The narrator makes the dressing table grand! Everyday appearance receives the equipment and solemnity of a heroic undertaking.|mirror
2|The guardian sees an uncertain danger|Ariel's warning cannot identify exactly what will go wrong. Suspense enters a polished world! The supernatural machinery magnifies anxieties that society treats as matters of reputation.|ghost
3|The game imitates a battle|The card contest becomes another heroic struggle. Such enormous language for social play! The mismatch teaches us how mock epic makes scale itself funny.|cards
4|A small tool carries the offence|Clarissa supplies scissors, and the Baron finds his chance. The grand conflict has tiny equipment! A cut curl becomes an injury to status and honour.|scissors
6|The advice cannot quiet the quarrel|Clarissa urges perspective on beauty and character. Will anyone hear her? The poem places judgement beside a society still committed to treating a curl as catastrophe.|book''',
'lyrical-ballads': '''1|The ordinary life becomes worth a poem|A rural person or familiar feeling can take centre stage. What a change in attention! Poetry asks us to look where established grandeur might not direct us.|village
2|A child's answer resists adult counting|We Are Seven sets lived attachment against the adult's arithmetic. Listen to the disagreement! Death has not removed the child's sense of family membership.|home
3|The strange voyage asks for belief|Coleridge gives the Mariner's impossible experiences emotional force. Can imagination make wonder matter? The collection joins supernatural strangeness with recognisable fear and guilt.|sea
4|Memory changes a returning landscape|Tintern Abbey looks at nature through years of remembered experience. The same place is not the same encounter! The changed speaker is part of what he sees.|river
6|The preface follows the experiment|Wordsworth later explains the poetry's aims. Read the theory beside the poems! Its claims grow from an artistic experiment rather than preceding every line unchanged.|book''',
'the-excursion': '''1|The walker carries another life|The Wanderer's experience gives conversation a practical history. Who speaks matters! Hope comes from a person formed by encounters, not from an abstract command to cheer up.|road
2|The abandoned cottage holds a story|Margaret's suffering is recalled within the rural setting. Stop and listen! A quiet place can contain losses that its surviving appearance does not announce.|home
3|The recluse has reasons for despair|The Solitary's sorrow and disillusionment are not empty moods. His listeners must attend! Any answer to hopelessness has to face the experiences that made it persuasive.|grave
4|The exchange cannot be won by a slogan|The speakers test beliefs through sustained conversation. What can another voice offer? The poem lets consolation struggle with objections rather than arriving effortlessly.|book
6|The local dead extend the argument|The Pastor's accounts bring particular lives into the debate. Philosophy gains names and places! Memory of a community makes abstract claims answerable to human experience.|village''',
'frankenstein': '''1|The listener also wants greatness|Walton longs for extraordinary discovery. Why begin with him? Victor's story is a warning addressed to someone whose ambition might repeat its central mistake.|ice
2|The maker flees the first need|The creature wakes into abandonment. What does newly made life need before knowledge or power? Victor's refusal of care makes creation the beginning of an obligation he avoids.|laboratory
3|A child becomes another victim|William dies and Justine is blamed. Victor knows more than he admits! His secrecy lets the consequence of his experiment spread into an innocent person's punishment.|grave
4|The hoped-for welcome ends in rejection|The creature approaches the De Lacey household seeking acceptance. How painful the reversal is! The learning that gave him hope cannot prevent fear from closing the door.|gate
6|Two lives are imagined beyond society|The promised companion might let the creatures leave human company. But Victor fears future harm! The proposed bargain joins compassion to consequences nobody can guarantee.|heart''',
'vanity-fair': '''1|The school gate opens onto unequal futures|Becky and Amelia leave with very different resources. Their friendship cannot remove class! One must manoeuvre where the other can initially rely upon family security.|gate
2|Charm learns to travel upward|Becky studies what wealthy households want to hear. Watch her skill! The society judging her ambition also rewards the appearances she learns to manufacture.|mask
3|The wedding does not settle devotion|Amelia marries George, whose loyalties remain unstable. Affection alone cannot make him faithful! Her ideal picture of love leaves painful evidence outside its frame.|heart
4|War interrupts the marriage market|Waterloo breaks the social manoeuvring with actual death. George is killed! The cost of history enters lives previously organised around money, attraction and advancement.|sword
6|A patient lover needs honest recognition|Dobbin's care persists, but idealising Amelia also has limits. Can she finally see him? The ending asks what devotion becomes when it meets a real person.|mirror''',
'in-memoriam-a-h-h': '''1|The name carries a missing voice|Hallam is present as memory rather than a living reply. Feel that absence! The poem's speaker must keep addressing an attachment that cannot answer in its old way.|letter
2|Words cannot equal the loss|The speaker questions whether poetry can carry grief faithfully. What can language do? Its inadequacy becomes one reason to continue the careful work of expression.|book
3|Another Christmas arrives without him|Repeated seasons measure both change and persistence. The familiar bells sound different! Time moves outward while feeling circles back toward the same missing friend.|clock
4|Nature gives an unsettling answer|The natural world's indifference troubles religious confidence. Can faith survive that evidence? The elegy lets doubt become part of its movement rather than suppressing it.|storm
6|The attachment becomes an inward influence|Hallam's remembered qualities continue working within the speaker's life. Love changes its form! The friend's absence does not prevent his influence from shaping present judgement.|heart''',
'the-return-of-the-native': '''1|The heath keeps its own rhythm|Human wishes enter a landscape older than their quarrels. Notice its persistence! Egdon's atmosphere makes ambition feel both intense and small beside a resistant environment.|mountain
2|Escape and return point opposite ways|Eustacia wants a larger world while Clym hopes to serve the place he left. Can love join those directions? Their deepest hopes already contain a conflict.|road
3|The wished-for teacher faces a different life|Clym's eyesight fails, and practical work replaces his imagined educational mission. Plans meet the body! His circumstances become another disappointment within the marriage.|stone
4|The closed door grows into a tragedy|Mrs. Yeobright's visit ends without the welcome she expects. A misunderstanding can travel far! What one person believes about that threshold deepens several lives' estrangement.|gate
6|The final journey does not explain itself|Eustacia goes toward escape in a storm and drowns. Hold the uncertainty! The circumstances support questions about accident and intention without settling her inner decision.|storm''',
'a-doll-s-house': '''1|The pet names define a role|Torvald's affectionate language keeps Nora small. Listen beneath its warmth! A household can make dependence sound loving while refusing the person's equal standing.|home
2|The borrowed money paid for care|Nora's hidden loan helped save Torvald. Her secret began in love! The law and their unequal marriage make that care vulnerable to judgement rather than gratitude.|coins
3|A threatened job becomes leverage|Krogstad fears losing his position and uses Nora's forgery. How tightly their needs connect! One household's respectability gives him power over another person's silence.|contract
4|The dance tries to hold back time|Nora's performance delays the letter's opening. Watch the desperation behind the entertainment! A cheerful surface becomes a defence against a truth she cannot yet control.|stage
6|The expected rescue does not arrive|Torvald worries about his own reputation when he reads the letter. Nora's imagined miracle collapses! The crisis reveals the marriage more clearly than the secret itself.|mirror''',
'tess-of-the-d-urbervilles': '''1|An old name promises a false road|The family hopes an ancestral claim can improve its fortunes. What might that hope cost Tess? Status sends a vulnerable young woman toward unequal power.|crown
2|The harmed woman carries the judgement|After Alec's exploitation, Tess faces condemnation that should not be hers. Pause before blaming! The novel asks us to see how social verdicts repeat an injury.|chains
3|The child's life is painfully brief|Tess cares for Sorrow and mourns his death. Her vulnerability contains tenderness! A damaged reputation cannot measure her capacity to love or the reality of her grief.|home
4|Two confessions receive unequal answers|Angel expects forgiveness for his own past but condemns Tess's. How stark the double standard! What he calls principle becomes a refusal of equal human understanding.|mirror
6|The hoped-for return arrives too late|Angel comes back after Tess has yielded to Alec's renewed pressure. The timing matters! A delayed change of judgement cannot restore the circumstances it helped destroy.|clock''',
'heart-of-darkness': '''1|The peaceful river holds another history|Marlow begins on the Thames, reminding listeners of its earlier darkness. Look at the frame! The critique of conquest reaches beyond the distant Congo alone.|river
2|The company's language conceals bodies|Civilisation and trade sound respectable beside actual suffering. Hear the mismatch! Bureaucratic purpose cannot explain away the human cost visible along Marlow's route.|chains
3|A name grows before its owner appears|Everyone seems to have an account of Kurtz. How large a reputation can become! The delayed meeting lets rumour construct a figure whose actual conduct will break the image.|letter
4|The river makes progress uncertain|Travel slows through danger and confusion. Marlow cannot see the whole system from the boat! Limited knowledge becomes part of the way the story reaches its listeners.|ship
6|The listener in Europe wants another truth|The Intended remembers an ideal Kurtz. Marlow's final lie protects that picture! Returning home does not make the violence easier to represent honestly.|mirror''',
'the-waste-land': '''1|A buried season becomes a refuge|Winter's apparent shelter seems easier than spring's awakening. What is painful about renewal? Desire and memory return with the new growth instead of staying safely numb.|garden
2|The city walks like a troubled memory|The crowd crosses London under a sense of spiritual exhaustion. So many bodies, so little connection! Urban movement becomes another image of life diminished within apparent activity.|city
3|A conversation cannot find an answer|The anxious room contains voices that struggle to meet. Listen to the gaps! Language keeps arriving without securing the intimate understanding its speakers need.|home
4|A warning follows the drowned merchant|Phlebas loses worldly calculation beneath the water. Remember the address to the living! The drowned figure makes mortality speak across the poem's shifting ranks and voices.|sea
6|The fragments do not become one easy tale|The ending gathers borrowed phrases and broken pieces. Where is the complete remedy? The poem preserves a search for order while refusing a simple repaired plot.|book''',
'a-passage-to-india': '''1|Courtesy crosses an official boundary|Mrs. Moore hears Aziz as a person rather than a colonial category. That small respect matters! An encounter can open a possibility that institutions make difficult.|temple
2|The good invitation carries unequal worlds|The gathering seems friendly, but each visitor brings assumptions. What does understanding require? Shared space alone cannot remove the politics shaping who feels at home.|hall
3|A question unsettles the excursion|Adela's expectations about discovering India meet a place she cannot easily interpret. The outing becomes uncertain! The desire for experience does not guarantee the ability to understand it.|cave
4|The accusation gives a group its certainty|Colonial solidarity moves faster than evidence. Watch the room close ranks! An uncertain personal experience becomes an apparently clear public judgement through unequal power.|chains
6|Withdrawal does not repair every relationship|Adela retracts the allegation, but humiliation and distrust remain. Justice can stop one wrong! It cannot instantly restore the friendships or confidence the accusation has injured.|letter''',
'the-old-man-and-the-sea': '''1|The boy keeps a different measure|Manolin sees more than a run of empty catches. What makes a fisherman worth loving? Practical failure has not erased his respect for Santiago's skill and character.|home
2|The old man chooses distance|Santiago goes beyond the usual fishing grounds. Hope takes him outward! The chance for a great catch also places him far from help when the struggle begins.|ship
3|The hand hurts but the line stays held|Pain makes endurance bodily and immediate. Feel the pressure! Admiration for the marlin does not make the work gentle or let Santiago avoid the costs of catching it.|rope
4|The opponent becomes a responsibility|Santiago recognises the fish's dignity while preparing to kill it. What a difficult bond! Respect and necessary violence remain together rather than cancelling each other.|sea
6|The shore reads the remains differently|Others see an immense skeleton; Santiago remembers the struggle. The evidence is incomplete! The boy's renewed care answers a loss that the size of the catch cannot fully express.|stone''',
'seize-the-day': '''1|The hotel gives proximity without comfort|Wilhelm lives near his father but remains emotionally stranded. How can closeness feel so distant? A shared address does not guarantee the understanding he urgently needs.|city
2|The successful father protects his distance|Dr. Adler reads the crisis through discipline and reputation. Wilhelm asks for more! Their exchange makes practical dependence inseparable from a son's hunger for recognition.|coins
3|The helpful talk has an uncertain price|Tamkin makes Wilhelm feel understood. That relief is powerful! Insight, performance and financial self-interest become difficult for a vulnerable listener to separate.|mask
4|The market refuses the rescue story|Prices move without regard for Wilhelm's need. What happens to a promised new beginning? The investment turns emotional hope into exposure to another impersonal system.|storm
6|The stranger gives grief somewhere to go|At the funeral, Wilhelm can cry without winning his family's approval. An unknown death opens a human connection! The release matters even while practical problems remain.|grave''',
'things-fall-apart': '''1|The feared father remains inside the son|Okonkwo measures himself against Unoka's failures. Listen to the fear beneath the strength! His wish to escape one example becomes a harsh rule for others.|mirror
2|The household learns what anger can do|Family members live with Okonkwo's violence as well as his achievement. Prestige has a private cost! Public standing cannot tell us everything about the people closest to him.|home
3|The warning offers a choice|Okonkwo is told not to participate in Ikemefuna's killing. He still acts! The tragic force lies partly in a chance for restraint that his fear refuses.|sword
4|The community can discuss its own customs|Obierika questions and reflects where Okonkwo insists. Hear the variety! Igbo life contains disagreement and judgement, not a single rigid voice awaiting outsiders to change it.|village
6|The written account shrinks a human world|The Commissioner's imagined paragraph erases complexity. What must be remembered against that reduction? Achebe's whole novel answers the tiny place colonial narration assigns the life.|book''',
'utopia': '''1|The traveller carries an invitation to doubt|Hythloday's confidence makes the island sound persuasive. Listen without surrendering judgement! A returned traveller's account can challenge society and still need questions of its own.|ship
2|The useful adviser faces a difficult court|More hopes wise counsel can work by degrees. Hythloday doubts the compromise! Their debate begins with what practical influence might cost a person's convictions.|crown
3|The hungry thief exposes a system|Harsh punishment comes after social arrangements have produced deprivation. What has the law left out? The argument moves from condemning an act toward asking how it arose.|chains
4|Shared goods rearrange daily needs|An imagined community without private ownership changes work and leisure. Try the comparison! Familiar economic habits stop looking inevitable once another arrangement can be described.|village
6|The attractive island still needs scrutiny|Toleration and regulation sit beside coercion and exclusions. Is a beautifully ordered society enough? The account's tensions keep the island from becoming a simple endorsed perfection.|mirror''',
'romeo-and-juliet': '''1|An inherited quarrel finds new bodies|The young lovers did not invent the feud. Yet it reaches them! Family names make ordinary affection politically dangerous before either can choose a different future.|sword
2|The party makes an unexpected meeting|Romeo enters the Capulet celebration and meets Juliet. What a reversal of purpose! Attraction crosses the boundary their families expect them to preserve.|hall
3|The window offers a private world|The balcony conversation imagines love beyond surnames. Hear the hope! Their intimacy can question the feud, but cannot make the public danger disappear.|moon
4|The wedding must remain hidden|The Friar hopes marriage can reconcile the houses. Such an ambitious remedy! Secrecy protects the union for the moment while making later misunderstandings harder to correct.|contract
6|The message misses the person who needs it|The sleeping potion depends upon communication. One missed letter changes everything! Romeo acts on the visible appearance of death rather than the hidden plan for reunion.|letter''',
'a-midsummer-night-s-dream': '''1|A daughter asks to choose|Hermia's wish conflicts with her father's preferred marriage. How narrow the court's permission is! The forest offers escape from a decision already claimed by authority.|gate
2|The ruler of fairies wants obedience too|Oberon's dispute with Titania echoes the human struggle over choice. Magic does not abolish power! The enchanted forest contains another contest of who may decide.|crown
3|The potion reaches the wrong eyes|Puck confuses the lovers and shifts their desires. What could be less reliable than sudden certainty here? An enchanted feeling can seem utterly sincere to its bearer.|apple
4|The friends become romantic rivals|Helena believes she is mocked, while Hermia feels displaced. Hear the hurt beneath the comedy! The confused admiration damages a friendship before the spell is repaired.|heart
6|A dream may conceal an unresolved question|Demetrius remains magically changed at the ending. Keep that detail! A harmonious wedding can leave uncertainty about the source and freedom of one person's love.|stars''',
'hamlet': '''1|The mother’s marriage sharpens the grief|Gertrude's rapid remarriage to Claudius troubles Hamlet. He is mourning more than a death! The familiar household has changed its loyalties before he can understand the change.|home
2|The ghost needs to be tested|A frightening message is not yet secure knowledge. Can Hamlet trust its source? His hesitation includes a real problem of judging evidence before committing an irreversible act.|ghost
3|The theatre makes an inward suspicion visible|Hamlet watches Claudius watch the represented murder. What a layered experiment! Performance offers a reaction he hopes can turn a private allegation into stronger conviction.|stage
4|A daughter loses the father she depended upon|Polonius's death leaves Ophelia exposed amid the court's conflicts. Her suffering is no side effect to forget! Revenge spreads beyond its announced target.|grave
6|The skull gives the argument a body|Yorick's skull returns childhood familiarity as mortal remains. Hold that image! Death stops being only a philosophical problem when a remembered person's body supplies its evidence.|stone''',
'king-lear': '''1|The loyal voice is banished too|Kent protests Lear's judgement and is expelled. Authority removes its own correction! Cordelia's silence and Kent's plain speech become two truths the king refuses to hear.|gate
2|The retained title cannot command care|Lear gives away power but expects its former protections. What remains of kingship? A name and retinue cannot force the daughters to honour the father he imagined they were.|crown
3|The forged letter knows its audience|Edmund uses Gloucester's expectations to make Edgar appear treacherous. Watch the method! False evidence works best when it offers a story the listener is ready to believe.|letter
4|The exposed king discovers other bodies|The storm makes hunger and shelter urgent. Lear sees the poor differently! Vulnerability begins teaching him what command had allowed him to overlook.|storm
6|The reunion cannot guarantee rescue|Cordelia forgives without asking for a new love test. The tenderness is real! Political defeat still threatens what moral recognition has at last made possible.|heart''',
'death-be-not-proud': '''1|The feared name meets a confident voice|Death is addressed as an opponent who has exaggerated its reputation. What a bold opening! The speaker changes the relationship from passive terror to active argument.|crown
2|The sleeping body suggests a different scale|If sleep refreshes, death might not be absolute catastrophe. Follow the analogy! Familiar rest is used to loosen the authority of the frightening final name.|bed
3|The supposed master waits upon others|Rulers, chance and desperate actions provide Death's occasions. Who commands whom? The sonnet's argument reduces the imagined sovereign to a dependent servant.|chains
4|Ordinary remedies rival the terrifying power|Drugs and charms can make people sleep too. The speaker presses his case! Death cannot claim unmatched grandeur merely because it produces an apparently deeper rest.|laboratory
6|The last wakefulness changes the verdict|Eternal waking is the argument's decisive belief. Notice the foundation! The final triumph depends upon Christian resurrection, not a claim that bodily dying never happens.|sunrise''',
'the-duchess-of-malfi': '''1|Rank tries to own a widow’s future|The brothers treat the Duchess's choice as family property. Hear the pressure! Remarriage becomes dangerous because a powerful household refuses her the authority to choose.|crown
2|A pregnancy makes privacy visible|Bosola watches the household for signs. An intimate future becomes evidence! The Duchess's family cannot remain safely separate from the people trying to control it.|mirror
3|The accusation is designed as protection|Antonio's apparent disgrace helps conceal an escape. What a risky reversal! She uses a false public story to defend a relationship that the truth would expose.|letter
4|The intelligent servant cannot claim innocence|Bosola sees enough to understand cruelty yet continues serving it. Knowing is not refusing! His divided conscience makes complicity more troubling than simple ignorance would.|mask
6|The late remorse cannot summon the dead|Bosola turns against the brothers after murder. The reversal matters—but not as repair! A conscience awakened too late must live inside the harm its actions helped create.|grave''',
'the-pilgrim-s-progress': '''1|The book becomes a burden as well as a guide|Christian's reading changes what his home means. Knowledge unsettles him! The journey begins because remaining comfortably unaware is no longer possible.|book
2|The mud makes despair a place|The Slough catches the traveller's fear and difficulty. How tangible the allegory becomes! An inward obstacle is given ground that the pilgrim must cross rather than merely describe.|river
3|Relief does not finish the road|The cross releases Christian's burden, but further trials wait. Remember the sequence! A decisive religious transformation begins another discipline instead of guaranteeing effortless arrival.|sunrise
4|An enemy challenges the traveller directly|Apollyon turns the road into combat. The symbolic struggle becomes bodily! Faith now has to endure opposition beyond the pilgrim's first fear of leaving home.|sword
6|A remembered promise changes the prison|The key called Promise opens captivity under Despair. What had been forgotten? A resource already available must be remembered before it can become practical freedom.|gate''',
'robinson-crusoe': '''1|The father offers a safer life|Crusoe's father praises a moderate station. The son hears—and leaves! The later account makes youthful restlessness answer an alternative it knowingly rejected.|home
2|The wreck leaves a store of fragments|Crusoe salvages tools and supplies before the ship breaks apart. Survival begins with what remains! The ruined vessel becomes the island household's first resource.|ship
3|The calendar keeps company with isolation|Crusoe marks time while ordering daily work. Why count days here? Routine makes solitary survival something more structured than an endless undifferentiated emergency.|clock
4|Illness opens another inward journey|Sickness and reflection lead Crusoe toward religious understanding. The island changes more than his skills! The remembered account turns material endurance into an interpreted spiritual life.|bed
6|The rescue carries an unequal name|Crusoe names Friday and makes him a subordinate companion. Look at both care and control! Ending loneliness does not make the relationship free of colonial hierarchy.|chains''',
'moll-flanders': '''1|The desired title promises security|Moll's wish to become a gentlewoman grows from vulnerability. What does respectable status buy? Her ambition seeks protection as well as admiration from the world judging her.|coins
2|The narrator chooses how much to confess|Moll recounts her past from a later position. Listen to the self-presentation! Remembering wrongdoing is also a chance to explain, soften and rearrange its meaning.|book
3|The overseas household hides another relation|The incest discovery overturns an apparent marriage and family security. What a trap in incomplete knowledge! Geography and new circumstances cannot automatically erase an unknown past.|ship
4|A changing costume protects the theft|Moll uses appearances to move through social spaces. Skill becomes dangerous! The same society that judges her also supplies the disguises through which she survives illegally.|mask
6|The confession meets a chance to continue|Newgate brings fear and spiritual counsel. Repentance is not the whole practical future! Transportation makes reform inseparable from another economic and geographic beginning.|gate''',
'gulliver-s-travels': '''1|The small court measures greatness by itself|Lilliput's confidence makes tiny rivalries look enormous. What are we invited to recognise? Changing physical scale exposes political habits that familiar size can conceal.|crown
2|A rescued ruler expects more service|Gulliver's help brings requests that offend his judgement. The giant cannot merely remain a tool! A grateful court still has ambitions the helper need not accept.|ship
3|The collector becomes the collected object|In Brobdingnag Gulliver is displayed and examined. The viewpoint flips! Someone who looked confidently at others now learns what it feels like to be a curiosity.|mirror
4|An elegant theory loses practical life|The academy's experiments pursue ingenuity at the cost of usefulness. How impressive failure can sound! Satire places everyday need beside grand claims of intellectual superiority.|laboratory
6|The ideal society has an excluded group|Gulliver admires the Houyhnhnms while recoiling from the Yahoos. His conclusion grows dangerous! A supposed moral ideal can encourage disgust toward the humanity he shares.|chains''',
'tom-jones': '''1|The foundling has a place but not a pedigree|Allworthy's kindness gives Tom a home. Yet the unknown origin matters! Society keeps asking who a person comes from before it asks how he behaves.|home
2|The correct manner can hide a selfish heart|Blifil performs virtue with calculated skill. Watch the difference! Tom's impulsive errors look worse on the surface than the quieter harm produced by polished self-interest.|mask
3|A lover cannot ignore the family plan|Sophia's affection meets her father's preferred match. Who chooses the future? The romance reveals how property and social judgement narrow a woman's practical freedom.|contract
4|The road teaches what the house had hidden|Tom meets people with different motives and circumstances. Experience makes judgement harder! The journey offers a moral education larger than the tidy categories he left behind.|road
6|The identity revelation does not create the heart|Tom's parentage improves his social position. Remember the difference! A recovered name can open doors without being the origin of the generosity already visible in him.|letter''',
'tristram-shandy': '''1|The first beginning refuses to stay first|Tristram reaches toward events before his birth. How can a life story start there? The attempt to explain everything immediately creates more beginnings than narration can manage.|clock
2|A hobby gives the mind its own map|Walter's theories and Toby's fortifications organise their interests. Every explanation has a rider! The narrator asks us to notice the habits through which people interpret experience.|stone
3|An accident outruns the theory|Tristram's name frustrates Walter's carefully imagined future. Life refuses perfect management! A small practical mishap becomes enormous inside a system already obsessed with its significance.|letter
4|The model battlefield shelters real feeling|Toby's military hobby is comic, but his kindness matters. Do not stop at the joke! The imagined campaign reveals a temperament gentler than the literal subject suggests.|garden
6|The blank space addresses the reader|Experimental pages ask us to imagine or pause. Who is finishing this story? The book makes its reader's participation visible within the very difficulty of telling a life.|book''',
'songs-of-innocence-and-of-experience': '''1|Two titles ask us to look twice|Innocence and experience are paired states of perception. Neither can simply cancel the other! The same human world becomes different when its promises meet its wounds.|mirror
2|The child’s trust deserves protection|Innocent voices offer joy and attachment, not merely ignorance. Hear their value! What experience exposes is partly the social failure to preserve the care that trust needs.|home
3|The soot enters a child’s working day|The chimney-sweeper's vulnerability places labour inside childhood. The dream of consolation cannot clean that fact away! Symbolic comfort and material injustice occupy the same poem.|fire
4|The fierce creature asks another creator’s question|The Tyger's beauty arrives with terror. How could this power be made? Wonder becomes difficult when creation includes what the gentle Lamb's image cannot explain.|forest
6|The street repeats the signs of constraint|London's voices carry suffering through public space. Listen to their pattern! Institutions and inward habits together make the city's boundaries feel harder to escape.|city''',
'tintern-abbey': '''1|Five years stand between two visits|The landscape is familiar, but the viewer has changed. What has returned with him? The poem lets elapsed time enter the present act of looking.|river
2|The remembered place once helped far away|Amid urban weariness, the landscape returned inwardly. Nature did not need to be physically near! Memory carried an earlier calm into a different setting.|city
3|The old delight cannot be recovered unchanged|The younger speaker's intensity has altered with age. Must that change mean only loss? The poem makes room for a quieter attention beside the missing exhilaration.|mountain
4|Human suffering enters the view|A deeper awareness accompanies nature now. Listen to the added note! Maturity gives the landscape an ethical meaning that youthful sensation did not fully contain.|heart
6|A sister can carry the place differently|Dorothy's future memory will belong to her own life. The speaker offers hope, not control! Shared experience can become separate inward resources after the visit ends.|garden''',
'the-prelude': '''1|The growing mind becomes the subject|The poem looks back to understand a vocation. How did this imagination form? Childhood is remembered as active development rather than a row of charming anecdotes.|book
2|The stolen boat brings an unexpected watcher|A mountain seems to loom after the child's excursion. Fear follows pleasure! The remembered scene gives nature power to work inwardly after the boat has returned.|mountain
3|Skating makes movement a kind of learning|The body explores speed, sound and the landscape's response. What does feeling teach here? The developing imagination grows through physical experience as well as books.|ice
4|The city offers another crowd of impressions|London enlarges the narrator's world with spectacle and distraction. Everything seems to demand attention! Growing perception has to learn which encounters deepen it and which merely scatter it.|city
6|A remembered moment can still repair|The spots of time preserve an inward strength. What remains from a difficult childhood scene? Its later power may nourish the mind precisely because memory has kept it vivid.|clock''',
'the-rime-of-the-ancient-mariner': '''1|The listener wants the wedding instead|The Wedding Guest begins unwilling to stop. Why must he hear this sailor? The frame makes storytelling itself the place where another person's experience changes a life.|hall
2|The killing has no satisfying explanation|The albatross dies by the Mariner's shot. The needless act matters! A welcoming living creature becomes the victim of power exercised without a clear necessity.|bow
3|The water cannot answer thirst|The ship lies surrounded by water its crew cannot drink. What a cruel reversal! The abundance of the setting makes their helplessness more frightening.|sea
4|Survival becomes the heavier sentence|Life-in-Death claims the Mariner while his companions perish. Being left alive is no triumph! The solitary witness must carry the eyes and memory of the dead.|ghost
6|The blessing arrives before calculation|He loves the water snakes spontaneously. Notice that change! Release begins with an unplanned recognition of other life, not a bargain calculated to remove his punishment.|river''',
'kubla-khan': '''1|The imperial command draws a boundary|Kubla orders an enclosed pleasure-dome. How confidently the decree sounds! Human design begins by imagining a beautiful space it can define and protect.|crown
2|The river ignores the enclosure’s promise|Alph passes toward caverns and darkness beyond clear measurement. Follow it! The designed garden belongs to a larger natural movement the ruler has not created.|river
3|The fountain brings power from below|The violent eruption breaks the stillness of the planned scene. What cannot be kept outside? Creativity appears as an energy whose force exceeds polite control.|fire
4|The shadow contains an impossible contrast|Sunlit pleasure and icy caves occupy one vision. Hold them together! The image's brilliance depends upon opposites that ordinary architecture cannot comfortably reconcile.|ice
6|The remembered song might rebuild the dome|The speaker wants to recover the Abyssinian maid's music. What a different maker now appears! Imaginative creation replaces the king's order with a desired act of listening.|music''',
'ozymandias': '''1|The ruler reaches us through a stranger|We do not meet a living king. A traveller speaks first! Distance and mediation begin undermining the direct authority that the monument once claimed.|road
2|The fallen face still knows how to command|The sculpted expression survives the ruined body. Look at the sneer! Political control has vanished, yet art preserves its posture for another audience to judge.|portrait
3|The artist’s hand has outlasted the throne|The sculptor understood the ruler's passions. What survived the making? A crafted image can preserve character after the government that paid for it disappears.|stone
4|The invitation asks for evidence nearby|The inscription orders mighty rivals to compare his works. So look around! The command's confidence makes the surrounding absence even harder to ignore.|crown
6|The desert gives no obedient answer|Sand stretches beyond the fragment. The empty space is the reply! The ruler's language remains inside a landscape that refuses to certify his promised permanence.|mountain''',
'ode-to-the-west-wind': '''1|The dead leaves are not the whole story|The wind scatters decay and carries seeds. Watch both motions! An apparent ending can also prepare a later life that is not yet visible.|forest
2|The hidden seed waits within the season|Dormancy resembles burial without being simple destruction. What must time still do? The ode's hope grows within nature's cycle rather than beyond all conditions.|garden
3|The clouds give the sky a rushing body|Storm imagery carries the wind upward. Its power crosses levels! The same force links fallen leaves to a vast atmospheric movement.|storm
4|The still sea is imagined waking|The Mediterranean and Atlantic respond to the wind's disturbance. Listen to the expanding scale! The speaker has not yet separated his own need from this elemental power.|sea
6|The poet wants to become the instrument|He asks the wind to use him as it uses leaves and forests. What might words carry? Personal weakness becomes a plea for a force that can scatter ideas.|music''',
'prometheus-unbound': '''1|The captive remembers his own hatred|Prometheus must face the curse he once pronounced. Resistance has an inward test! Refusing oppression does not automatically prevent its anger from entering the resister.|chains
2|The recalled curse is answered by mercy|He withdraws the spirit of hatred rather than praising Jupiter. Hear the difference! Compassion is imagined as another form of power, not as submission to the tyrant.|heart
3|The torment reaches through fearful visions|The Furies try to make suffering extinguish hope. Can he keep attention beyond pain? Endurance is tested where despair claims that nothing outside the present wound matters.|ghost
4|The beloved’s journey searches for understanding|Asia approaches Demogorgon through imaginative movement. Love does not stand still! The drama connects emotional commitment with an inquiry into how domination might end.|road
6|The changed world needs more than a new ruler|Jupiter's fall opens renewal, but the final vision reaches into relationships. Remember the ambition! Freedom is imagined as transformed life rather than a transferred throne.|sunrise''',
'ode-to-a-nightingale': '''1|The beautiful song makes the listener ache|Pleasure begins as numbness and pain. What an unexpected welcome! The bird's apparent happiness exposes the listener's inability to share it without feeling his own burden.|bird
2|The imagined drink promises distance|Wine becomes a wish to leave ordinary care behind. The request is poetic! He imagines escape from a condition, not simply a refreshing cup beside the bird.|coins
3|The human world enters the comparison|Illness, ageing and bereavement crowd the thought. The bird's freedom grows by contrast! Its imagined ease is heard through everything the human listener cannot forget.|grave
4|The darkness makes imagination more necessary|Poetry carries him where eyesight cannot clearly follow. Listen for the other senses! An inward journey takes shape while the actual setting remains partly unseen.|moon
6|The same song seems to cross centuries|The voice connects imagined earlier hearers and stories. What kind of immortality is this? Recurrence belongs to the song and imagination, not an endlessly living individual bird.|book''',
'to-autumn': '''1|The season works with the sun|Autumn's fullness comes through a partnership of weather and growth. Look closely! Ripeness is a process shaped across fields and orchards, not a trophy already finished.|sunrise
2|The bees mistake abundance for endlessness|Warmth and flowers seem to continue without limit. What a gentle warning! The season's generosity can make its approaching change difficult to imagine.|garden
3|The resting figure gives time a body|Autumn is imagined lingering among harvested work. There is no urgent conquest here! The poem invites attention to the pause within a process.|home
4|The cider press measures a patient ending|The last juice falls slowly. Watch without rushing! Value remains within completion's small movements rather than only in the final collected product.|clock
6|The evening chorus belongs to this season|Gnats, lambs and birds make their own sounds. Why demand spring's music? The autumnal world deserves to be heard in its present voice.|bird''',
'don-juan': '''1|The narrator interrupts his own hero|Byron's voice keeps competing with Juan's adventures. Who owns the journey? The telling exposes the beliefs a conventional heroic narrative might ask us to accept quietly.|book
2|The scandal gives the traveller a departure|An affair sends Juan away rather than confirming noble achievement. What a crooked beginning! The hero's movement grows out of embarrassment and appetite as much as choice.|ship
3|Hunger strips the travellers’ manners|The wreck makes survival more urgent than polite appearances. Watch necessity work! Social confidence proves fragile when the structures supplying food and safety disappear.|sea
4|The island’s freedom depends upon absence|Juan and Haidée love while Lambro is away. Their happiness has a condition! The idyllic setting cannot permanently exclude the authority that claims to own it.|garden
6|The polished society offers another disguise|English fashionable life surrounds appetite with respectable forms. Hear the satire underneath! Changed geography does not stop institutions from making self-interest look admirable.|mask''',
'goblin-market': '''1|The sales pitch offers delicious certainty|The goblins call their fruits with irresistible variety. Listen to the promise! Desire is encouraged before the buyer knows what kind of price the market will demand.|apple
2|A lock of hair becomes the payment|Laura has no ordinary coin and gives part of herself. The bargain is intimate! Consumption begins by exposing a personal vulnerability rather than merely exchanging spare money.|cloth
3|Only one sister still hears the vendors|Laura's craving meets the vanished call, while Lizzie can hear it. What isolates her? Their formerly shared world now contains an unequal access that worsens desire.|music
4|A remembered death makes the risk clearer|Jeanie's fate gives the sisters an earlier warning. Knowing does not cure the craving! Memory makes danger visible without automatically supplying a way out.|grave
6|The refusal turns invitation into assault|Lizzie will not consume the fruit on the goblins' terms. Their friendliness breaks! A coerced market reveals what the earlier language of temptation concealed.|chains''',
'pride-and-prejudice': '''1|The first slight helps write the future|Darcy's proud manner gives Elizabeth a ready judgement. How quickly an impression becomes a story! Later information will enter a mind already inclined to believe the worst.|mirror
2|The charming witness has a motive too|Wickham's account flatters Elizabeth's dislike of Darcy. Listen to the advantage! An appealing speaker can make unreliable evidence feel personally satisfying.|mask
3|Charlotte chooses within a narrower field|Her marriage to Collins buys security at a cost Elizabeth dislikes. What are the available choices? The novel asks readers to compare circumstances before judging a compromise.|coins
4|The proposal arrives carrying an insult|Darcy declares affection while stressing social objections. No wonder Elizabeth resists! Love spoken from unequal assumptions cannot expect gratitude merely for announcing itself.|heart
6|The rescue happens beyond the performance|Darcy helps secure Lydia's marriage without seeking public applause. Here is useful evidence! Character becomes clearer through costly action than through an attractive account of oneself.|letter''',
'sense-and-sensibility': '''1|The household’s future has a smaller purse|The Dashwood women lose familiar security after their father's death. Affection meets arithmetic! Reduced means shape where they live and what relationships appear possible.|coins
2|Elinor must interpret a guarded attachment|Edward's affection seems real, but obstacles remain unclear. What can restraint protect? She feels deeply while trying not to claim a certainty the evidence cannot give.|heart
3|A confidence requires painful silence|Lucy's secret prevents Elinor from freely explaining her suffering. The quiet sister bears more than others see! Composure becomes an effort, not an absence of emotion.|letter
4|The charming past contains another harmed woman|Brandon's account exposes Willoughby's conduct. A romantic manner cannot answer that history! Marianne must revise the connection between intense feeling and trustworthy care.|book
6|The recovery changes how feeling is used|Marianne does not simply stop having passions. She questions her conduct! Strong emotion can remain valuable while learning to attend to other people and consequences.|garden''',
'emma': '''1|A successful match gives Emma too much confidence|Miss Taylor's marriage looks like proof of Emma's skill. What if the evidence is weaker? One pleasant outcome becomes permission to direct another person's future.|heart
2|Harriet’s existing affection is treated as improvable|Robert Martin's kindness loses to Emma's imagined social promotion. Look at the judgement! Status makes a real attachment seem less valuable than an attractive speculation.|coins
3|The wrong suitor exposes the wrong reading|Elton's proposal shows how Emma has misread his attentions. A confident story collapses! Other people have intentions that her elegant matchmaking plot cannot assign to them.|mirror
4|The hidden engagement has serious stakes|Frank's playful behaviour protects a secret at Jane's expense. What does Emma fail to see? Another woman's vulnerability sits beneath the amusement she enjoys.|letter
6|A wounded neighbour needs actual attention|After Box Hill, Emma visits Miss Bates with a changed purpose. Remorse must travel beyond the self! Repair begins through care for the person the joke injured.|home''',
'jane-eyre': '''1|The child wants justice, not merely comfort|Jane resists the unfair treatment at Gateshead. Hear the strong voice! Her later search for love begins with an earlier insistence that her experience must count.|home
2|The school’s hardship contains a different friendship|Helen Burns offers Jane another moral presence amid neglect. Care is not the institution itself! A particular person's tenderness changes what suffering teaches the child.|heart
3|The employer is also a person she can answer|Jane's conversations with Rochester cross rank through wit and honesty. Something reciprocal begins! Their affection matters because she can speak, not only admire from below.|book
4|The hidden wife makes the offer impossible|Jane learns that Rochester's marriage still exists. Feeling cannot erase another life! Her departure protects conscience even while costing the love and security she wanted.|chains
6|The inheritance changes the terms of return|Jane gains money and kinship before returning to Rochester. Her choice is less dependent! The ending joins affection to a practical independence she had previously lacked.|coins''',
'wuthering-heights': '''1|The household is already difficult to read|Lockwood misunderstands the people he meets. What a troublesome doorway into a story! Nelly's later account has to untangle appearances filtered through his first mistaken assumptions.|gate
2|The child’s belonging is made insecure|Heathcliff's arrival changes family relationships, and later hostility degrades him. Affection grows beside humiliation! The remembered childhood contains the injuries that revenge will keep repeating.|home
3|The marriage separates two claimed identities|Catherine chooses Edgar while declaring a profound bond with Heathcliff. How can both decisions stand? Social safety and inward attachment pull her future in incompatible directions.|heart
4|The returned outsider learns the uses of property|Heathcliff's new resources let him control households and inheritance. Money becomes revenge! The power he lacked as a child is used to reproduce another generation's captivity.|coins
6|Reading creates a different kind of intimacy|Cathy and Hareton share learning where earlier relationships denied it. What can care interrupt? Their bond offers a practical alternative to love expressed through possession and degradation.|book''',
'great-expectations': '''1|The stolen food begins a lasting connection|Pip helps the escaped convict out of fear, then carries the memory. Who could predict its return? A small frightened act will reshape the life he imagines he has earned.|apple
2|The beautiful house manufactures shame|Estella's contempt makes Pip ashamed of his ordinary home. Listen to the injury! His ambition begins by accepting someone else's hierarchy as a judgement of his own worth.|home
3|The anonymous gift permits a flattering guess|Pip assumes Miss Havisham is preparing him for Estella. What convenient evidence he lacks! Unnamed generosity becomes a romance written largely by his own desire.|letter
4|The gentleman becomes unkind to the loyal man|Pip's embarrassment about Joe reveals a cost of advancement. Is refinement improving his heart? Social aspiration teaches him to mistreat someone whose affection remains steady.|mirror
6|The rescued convict becomes a human companion|Pip's attempt to help Magwitch changes their bond. Gratitude replaces disgust! A failed escape can still mark a real moral growth in the person undertaking it.|ship''',
'a-tale-of-two-cities': '''1|A life is being recalled from imprisonment|Manette's return begins as a fragile recovery, not instant normality. Lucie's care matters! Political release must be followed by the slow rebuilding of an injured human world.|chains
2|A resemblance makes innocence harder to judge|Carton's likeness helps Darnay at trial. Notice the possibility planted here! Two faces that confuse identification will later permit a different kind of deliberate substitution.|mirror
3|A family name carries an unchosen history|Darnay rejects aristocratic cruelty, but others remember his lineage. Can a personal decision erase collective injury? The revolutionary court will answer more harshly than his intentions deserve.|crown
4|The past has left a written witness|Manette's prison testimony records the family's violence. A buried document returns! The evidence that once preserved suffering now helps condemn the man his daughter loves.|letter
6|The promise has to become an act|Carton's earlier devotion finds a practical form through substitution. Watch the transformation! A life he has judged wasted becomes a chosen protection for another person's future.|heart''',
'oliver-twist': '''1|Hunger asks an ordinary question|Oliver wants enough food. The institution hears defiance! Remember the simplicity of the request beside the elaborate moral judgement imposed upon a vulnerable child.|apple
2|A welcoming group has another use for him|Fagin's circle seems to offer belonging. What does the shelter require? A lonely child can be drawn into exploitation through the very need for company and safety.|mask
3|The benefactor sees a person rather than a category|Brownlow's kindness interrupts the criminal label attached to Oliver. Look at the difference! Protection begins when someone attends to the child rather than a convenient suspicion.|home
4|A forced crime turns the victim into apparent evidence|Oliver is made to assist burglary and is injured. His participation is coerced! The novel asks us not to mistake an endangered child's presence for a freely chosen identity.|chains
6|The helper cannot escape the world she exposes|Nancy's disclosure protects Oliver while increasing her own danger. Her courage is costly! Another person's rescue can depend upon someone who never receives the same freedom.|letter''',
'bleak-house': '''1|The fog belongs to more than weather|Chancery's obscurity reaches across lives and social ranks. How does anyone find a clear path? The atmosphere makes institutional delay something a reader can almost breathe.|city
2|Two narrators give two kinds of seeing|Esther's modest account sits beside a sharper public voice. Listen to both! One life cannot supply the whole perspective on an institution affecting so many people.|book
3|The expected inheritance begins consuming the heir|Richard keeps investing his future in the lawsuit. What if waiting itself is the trap? Hope becomes the mechanism through which the process drains him.|coins
4|The hidden mother faces an exposed past|Lady Dedlock's secret cannot remain safely inside rank and elegance. Legal knowledge becomes pursuit! An intimate history enters a system that can weaponise its discovery.|letter
6|The search loses the person it was chasing|Esther reaches her mother too late. A discovery is not a rescue! The ending makes the limits of restored knowledge painfully visible beside the law's exhausted promise.|grave''',
'middlemarch': '''1|The desired greatness is assigned to the wrong man|Dorothea imagines helping Casaubon's grand scholarship. How generous—and how mistaken! A wish for purpose can overlook the actual limitations of its chosen object.|book
2|The reformer also needs a household|Lydgate's medical hopes cannot float above money and marriage. The town will test both! Professional ideals have to live inside the practical relationships that support or constrain them.|home
3|The widow receives a condition disguised as protection|Casaubon's will tries to control Dorothea's future relation to Will. Death does not end possession! An inheritance becomes another tool for continuing authority over choice.|contract
4|The shared marriage contains different desired futures|Rosamond and Lydgate disagree about status, spending and vocation. Who must adapt? Private expectations become financial constraints that reshape what he can do publicly.|coins
6|Sympathy must pass through an injured first impression|Dorothea's visit to Rosamond requires seeing beyond jealousy and humiliation. What an inward act! Attention to another person's pain becomes a more useful achievement than imagined grandeur.|heart''',
'the-mill-on-the-floss': '''1|The bright girl needs more room than she receives|Maggie's curiosity and affection meet the family's narrower expectations. Her mind matters! Repeated correction teaches her that the wish to belong may conflict with being herself.|book
2|An adult quarrel becomes the children’s boundary|Mr. Tulliver's hostility to Wakem limits Maggie's relation to Philip. What have they inherited? A business conflict is passed down as a rule for personal attachment.|chains
3|Renunciation promises a way to quiet desire|Maggie turns toward self-denial, hoping to bear disappointment. Listen to the need beneath it! Suppressing longing may bring discipline without providing the affection she still seeks.|temple
4|The boat takes a hesitation beyond easy recall|Maggie's journey with Stephen carries them too far. Desire now has public consequences! An inward conflict becomes a situation others can judge without understanding its whole history.|river
6|The return asks for a difficult kind of courage|Maggie refuses a future that would harm others and comes back. Doing what she judges right still costs her! Social condemnation does not carefully measure the decision.|gate''',
'silas-marner': '''1|The trusted community condemns the wrong man|Silas's betrayal damages his faith in people and belief. What can remain after such judgement? Withdrawal becomes protection when the place of belonging has made him unsafe.|chains
2|The coins offer a controllable companionship|Silas counts money where he once relied upon people. The substitute feels secure! Its apparent steadiness cannot answer the human need that distrust has driven into silence.|coins
3|A respectable father hides an unacknowledged child|Godfrey's fear of disclosure leaves another household vulnerable. Look behind the public appearance! Concealed responsibility can make a seemingly honourable person dependent upon continuing neglect.|mask
4|The open doorway admits another kind of treasure|Eppie wanders into the cottage after her mother's death. Life enters where gold has vanished! Silas answers by caring, not merely by admiring the unexpected visitor.|gate
6|The later claim cannot buy the earlier care|Godfrey offers Eppie wealth and his name after years of absence. What makes a father now? The relationship formed through everyday responsibility resists being replaced by a delayed entitlement.|heart''',
'the-picture-of-dorian-gray': '''1|The beautiful face invites another man’s influence|Lord Henry's talk makes youth seem a value above consequence. Listen critically! The persuasive voice changes how Dorian interprets the body and future he has received.|mirror
2|The actress becomes an object of admiration|Dorian loves Sibyl's performance before understanding her separate life. What happens when art stops satisfying him? His attachment reveals a demand for an image rather than care for a person.|stage
3|The first changed detail makes guilt visible|The portrait alters after cruelty while Dorian's face remains admired. Such a dangerous division! He can hide evidence without having undone the action that produced it.|portrait
4|The locked room permits another public life|Dorian keeps the canvas away from other eyes. Secrecy preserves the admired surface! The wider distance between appearance and consequence makes further wrongdoing easier to conceal.|gate
6|The threatened witness recalls an earlier victim|Sibyl's brother pursues Dorian while the past presses inwardly too. Escape is not innocence! A face that defeats identification cannot remove the history behind the danger.|ghost''',
'the-importance-of-being-earnest': '''1|The useful name creates two social selves|Jack's town identity lets him behave differently from the country guardian. How convenient! The comedy begins where responsibility can be evaded through an invented person.|mask
2|An invalid friend supplies another exit|Algernon's Bunbury makes absence sound like duty. Listen to the excuse! A supposedly caring obligation becomes the instrument for avoiding obligations he actually has.|letter
3|The marriage interview counts the wrong evidence|Lady Bracknell tests income and parentage more readily than character. The handbag alarms her! A social system can make an accidental origin more important than present conduct.|coins
4|The women recognise a shared desired name|Gwendolen and Cecily each claim an Ernest. A polite conversation turns competitive! Their attachment to a label helps keep the men's deception attractive until its contradictions surface.|heart
6|The lost manuscript carries a recovered baby’s history|Miss Prism explains the exchange at the station. What a material clue! Jack's apparently impossible pedigree has depended upon the movement of an ordinary bag.|book''',
'strange-case-of-dr-jekyll-and-mr-hyde': '''1|The respectable will protects an alarming stranger|Utterson sees Hyde's power over Jekyll's property. How could the arrangement make sense? He tries ordinary explanations before the story reveals a possibility beyond them.|contract
2|The doctor reassures without supplying understanding|Jekyll claims he can dismiss Hyde when he chooses. Hear the confidence! A statement of control is not the same as evidence that the control remains secure.|mask
3|The murder gives the hidden life a public cost|Hyde kills Carew and disappears. Jekyll's outward reform looks hopeful! Yet apparent withdrawal cannot by itself guarantee that the violent identity has been contained.|sword
4|The witness receives more truth than he can bear|Lanyon sees the transformation and cannot recover from its shock. Knowledge brings its own wound! The delayed document preserves evidence through a person it has already harmed.|letter
6|The chemical supply becomes a terrible limit|The needed salt cannot reliably be replaced. What has the experiment depended upon? A supposed mastery of moral division ends in a material condition Jekyll cannot command.|laboratory''',
'dracula': '''1|The host’s courtesy hides the locked door|Harker discovers he is not free to leave the castle. What changed in hospitality? Polite forms make captivity harder to recognise until their actual limits become visible.|gate
2|The arriving ship brings a missing human crew|The sea voyage enters England as a strange record of disappearance. Watch the evidence accumulate! The danger reaches another community before anyone can name its mechanism clearly.|ship
3|The illness defeats the first medical explanation|Lucy's decline persists despite repeated help. Conventional care is necessary but incomplete! The investigators must change their assumptions before knowledge can become effective protection.|bed
4|The frightening victim needs release from the predator|Lucy's transformation makes saving her look unlike ordinary rescue. The violence is disturbing! The hunters understand it as freeing the person from a continued undead harm.|grave
6|The excluded partner possesses essential knowledge|Leaving Mina out appears protective but proves dangerous. Listen to what cooperation requires! Someone treated only as a vulnerable dependent is also a vital participant in understanding the threat.|book''',
'a-portrait-of-the-artist-as-a-young-man': '''1|The earliest language gives the world its shape|Stephen begins inside sounds and words received from others. The style grows with him! His later artistic independence has to develop from language that first belonged to family and culture.|music
2|The dinner table makes history intimate|The Parnell argument turns politics into family conflict. How quickly loyalties divide! National debate reaches the child's life through voices carrying anger, conviction and affection.|hall
3|The complaint becomes an early public act|Stephen protests unfair punishment at school. A voice can answer authority! The success matters because he experiences his own account being heard rather than silently accepting another judgement.|letter
4|The sermon turns desire into terror|Religious teaching makes guilt intensely bodily and imaginative. Fear offers a complete explanation! Stephen's response shows how institutional language can organise an inward experience with enormous force.|fire
6|The admired image opens another vocation|The girl by the sea becomes an imaginative revelation. He does not possess her life! The encounter changes his sense of what attention and artistic creation might become.|sea''',
'dubliners': '''1|A shared city is not a shared protagonist|These lives inhabit Dublin but belong to distinct stories. Keep the boundaries! Their recurring difficulties make a pattern without turning the collection into one continuous adventure.|city
2|The bazaar arrives too late for the fantasy|The boy in Araby reaches an unromantic commercial place. His imagined quest falters! Desire meets ordinary money, tired conversation and a vision of his own vanity.|coins
3|The leaving woman cannot cross the final threshold|Eveline stands before escape but remains held by fear and duty. What makes movement impossible? A possible future loses to the powerful weight of the life already known.|gate
4|The visiting friend makes a private life feel small|Little Chandler compares himself with Gallaher. Admiration becomes dissatisfaction! A dream of artistic freedom collides with insecurity and the actual care demanded at home.|book
6|The successful speech cannot prepare the listener|Gabriel's social confidence meets Gretta's memory of Michael Furey. How little he knew! The person closest to him contains a past his practiced eloquence cannot command.|music''',
'mrs-dalloway': '''1|The flowers carry more than decoration|Clarissa's errand moves through a city layered with memory. Look at an ordinary day! Buying something for a party can open questions about the choices shaping a whole life.|garden
2|The returning friend revives an unchosen future|Peter Walsh brings former intimacy and disagreement into the present. What might another marriage have meant? Memory does not merely recover events; it tests paths the speaker did not take.|letter
3|The city shares space without sharing understanding|Clarissa and Septimus inhabit the same public world without meeting. Their proximity is a formal link! Separate inner lives can reveal different costs of a society's accepted appearances.|city
4|The medical remedy threatens another loss|Separation is proposed for Septimus, heightening his terror. Care needs to listen! A confident treatment can feel coercive when it refuses the sufferer's particular experience.|chains
6|The reported death enters the host’s privacy|Clarissa withdraws briefly from the party to reflect. An unknown life changes her inward moment! Their connection is made through the news and her response, not an invented meeting.|home''',
'to-the-lighthouse': '''1|The child hears a judgement of possibility|James hopes for the trip while his father's forecast denies it. Such a small exchange, such strong feeling! The desired lighthouse already holds a family relationship.|sea
2|The painter needs room to trust her looking|Lily resists judgements about women's artistic limits. Who decides what she can make? Finding a composition also becomes an effort to preserve an independent vision.|portrait
3|The dinner’s harmony is a temporary achievement|Mrs. Ramsay draws different people into a shared atmosphere. Notice the labour of connection! The moment matters precisely because nobody can guarantee it will last.|hall
4|The darkened house keeps receiving time|The building changes through weather while human deaths are briefly reported. What continues without us? An apparently empty place makes the passing years materially visible.|ghost
6|The arrival cannot restore the first wish|James reaches the lighthouse with a changed family. He sees differently now! A delayed destination may offer recognition without returning the vanished people and feelings of childhood.|ship''',
'sons-and-lovers': '''1|The strained marriage redirects affection|Gertrude's disappointment in Walter draws emotional investment toward the children. Watch the changing household! A marital wound helps organise bonds that later prove difficult to loosen.|home
2|The elder son carries the first hope|William's departure seems to promise advancement, then his death intensifies loss. The family future changes! Paul receives an emotional weight shaped before his own adult choices.|grave
3|The artist still answers the household’s claim|Paul's work opens possibilities while closeness to his mother persists. How can independence grow? His development remains tied to a relationship that gives support and constrains separation.|portrait
4|The loved person can feel like a demand|Miriam offers deep companionship, but Paul experiences it ambivalently. Hear both needs! Intimacy becomes difficult when affection is felt as another claim upon an unsettled self.|book
6|The bereaved son faces an unorganised future|Gertrude's death removes a central bond without supplying freedom's next step. What now? The absence exposes how hard it is to choose life when dependence has shaped its meaning.|road''',
'the-love-song-of-j-alfred-prufrock': '''1|The invitation falters before the first decision|Prufrock begins with imagined movement, yet hesitation enters immediately. Will he actually go? The dramatic energy lies within a mind rehearsing a life it struggles to enter.|road
2|The room contains an imagined audience|The women and their conversation become a tribunal in his thoughts. Listen to the anticipation! Their actual judgement matters less than the judgement he keeps supplying in advance.|hall
3|A promise of more time postpones the present|There will be time, he repeats. How comforting—and how costly! The imagined future makes the current moment seem unnecessary, allowing avoidance to borrow the form of preparation.|clock
4|The observed body becomes another argument against action|He worries about ageing, hair and dress. Look at the inward gaze! The anticipated look of others is already doing its work before a decisive encounter occurs.|mirror
6|The small role protects him from a large attempt|He distances himself from Hamlet's grandeur. A modest self-image can be perceptive! It can also justify remaining safely beside the action instead of risking a central choice.|stage''',
'four-quartets': '''1|The four places hold different returning questions|Burnt Norton, East Coker, The Dry Salvages and Little Gidding anchor the sequence. Follow the variation! Each meditation revisits time without becoming another chapter of one literal journey.|road
2|The unchosen garden opens a possibility|An imagined path holds what might have been. What can the present contain? Memory, possibility and attention make chronological order only part of the experience being examined.|garden
3|Generations loosen the claim to mastery|East Coker links origins and endings through recurring human lives. Knowing is not owning! The meditation asks experience to become humility rather than an accumulating claim of certainty.|home
4|The river continues beyond prediction|The Dry Salvages places people beside elemental movement. Hear the uncertainty! Attention matters partly because the future cannot be secured by confident calculation alone.|river
6|The repeated words return with altered weight|Patterns gather across the separate poems. Read the echoes! Understanding grows through revisiting an image, not only through reaching a new statement farther along a straight line.|music''',
'the-second-coming': '''1|The circling bird no longer hears command|The falcon travels beyond the falconer's reach. What keeps an order together? The opening image lets lost communication become visible before the poem names wider collapse.|bird
2|The centre cannot organise the scattered world|Disintegration grows from the first image into public crisis. The movement feels unstoppable! A controlling structure has lost the power its familiar shape once promised.|storm
3|Confidence is not distributed according to goodness|The best hesitate while destructive intensity grows loud. Listen to the inversion! Certainty and moral worth are dangerously separated in the poem's historical vision.|crown
4|The expected revelation receives a different visitor|The phrase Second Coming prepares a Christian frame, but the vision unsettles it. What is arriving? Familiar language becomes the doorway to an unfamiliar and frightening figure.|ghost
6|The question refuses to give us a safe timetable|The beast moves toward an imagined birth while the poem remains uncertain. Remember the form! This symbolic vision is a disturbing question, not a factual prediction with verified dates.|stars''',
'sailing-to-byzantium': '''1|The young world continues without the ageing observer|Birds, fish and lovers move through generation and pleasure. He sees vitality everywhere! Yet the abundant scene offers little place for the body's felt decline.|garden
2|A lasting work suggests another scale of life|The speaker contrasts natural cycles with cultivated form. What could endure? The desire for art grows from mortality, not from an absence of admiration for the living world.|book
3|The bodily limit does not silence the possible song|The aged self imagines spiritual work beyond physical weakness. Hear the effort! The wish for transformation begins inside the very body it wants to exceed.|music
4|The destination names a hoped-for order|Byzantium offers an imagined meeting of sacred and artistic life. This is a symbolic voyage! The city becomes a way to seek value rather than simply a travel recommendation.|ship
6|The crafted bird would still need an audience|The imagined golden form sings to a court. What kind of permanence is desired? Art remains a relationship to listeners even when the speaker dreams of leaving natural life.|bird'''
}

# Place expanded moments beside their actual event, before the next consequence.
# These anchors follow the previous seven-scene catalogue, not a generic pattern.
ANCHORS={
    'hamlet':{'The skull gives the argument a body':5},
    'romeo-and-juliet':{'The wedding must remain hidden':3},
    'macbeth':{'The crown makes another man frightening':3},
    'the-tempest':{'A father controls the telling':1},
    'frankenstein':{'A child becomes another victim':4,'The hoped-for welcome ends in rejection':3,'Two lives are imagined beyond society':5},
    'the-return-of-the-native':{'The wished-for teacher faces a different life':4,'The closed door grows into a tragedy':6},
    'tess-of-the-d-urbervilles':{'Two confessions receive unequal answers':6},
    'the-waste-land':{'A warning follows the drowned merchant':6},
    'the-old-man-and-the-sea':{'The shore reads the remains differently':7},
    'seize-the-day':{'The helpful talk has an uncertain price':4,'The market refuses the rescue story':6,'The stranger gives grief somewhere to go':7},
    'things-fall-apart':{'The warning offers a choice':2}
    ,'the-rime-of-the-ancient-mariner':{'The blessing arrives before calculation':5}
}

def expand_and_tell(stories):
    import re
    companions={
        'beowulf':{'Unferth':'Danish courtier who questions Beowulf’s boast'},
        'king-lear':{'Kent':'Loyal servant banished for plain speaking','The Fool':'Companion whose wit questions Lear'},
        'frankenstein':{'William':'Victor’s younger brother','Justine':'Woman wrongly blamed for William’s death','The De Laceys':'Family observed by the creature'},
        'things-fall-apart':{'Unoka':'Okonkwo’s father whose example he fears','Uchendu':'Maternal uncle offering counsel in exile','The District Commissioner':'Colonial official who reduces the life to an account'},
        'pride-and-prejudice':{'Charlotte Lucas':'Elizabeth’s friend choosing financial security','Mr. Collins':'Clergyman whose proposal Elizabeth refuses'},
        'the-pilgrim-s-progress':{'Apollyon':'Allegorical enemy opposing Christian'},
        'the-mayor-of-casterbridge':{'Newson':'Sailor and Elizabeth-Jane’s father'},
        'the-merchant-of-venice':{'Lorenzo':'Jessica’s lover'},
        'twelfth-night':{'Maria':'Author of the forged letter to Malvolio'},
        'as-you-like-it':{'Phoebe':'Shepherdess attracted to Ganymede'}
    }
    for s in stories:
        for name,role in companions.get(s['id'],{}).items():
            if not any(c['name']==name for c in s['characters']):s['characters'].append(dict(name=name,role=role))
    openings=['Come closer!', 'Now watch!', 'Look a little closer!', 'Listen to this!', 'Here is what matters!', 'Stay with the story!', 'Now turn the page!', 'The scene changes!', 'What do you notice?', 'Keep your eyes on this moment!', 'What will this mean?', 'Carry this image with you!']
    questions={
        'heart':'What will affection ask of them now?', 'mask':'Who can see beneath that appearance?',
        'letter':'Who will believe the words—and who will pay for believing?', 'contract':'What happens when a promise meets its cost?',
        'coins':'Can money give them what they really need?', 'crown':'What does this power demand in return?',
        'grave':'What can the living still carry forward from this loss?', 'storm':'Which hope can survive the change?',
        'book':'What changes when this story is finally understood?', 'gate':'What waits on the other side of that decision?',
        'mirror':'Can the first impression still be trusted?', 'sea':'What will the journey ask of the traveller?',
        'home':'Will this place still mean safety?', 'chains':'Who has the power to let someone go?',
        'garden':'What might grow from this moment?', 'stage':'Who is performing—and who is being persuaded?',
        'clock':'How much time does the choice still have?', 'sword':'Who will bear the cost of this conflict?',
        'ghost':'What has returned that the present cannot ignore?', 'river':'Where will this movement lead?',
        'forest':'What can be discovered beyond the familiar path?', 'stars':'What can this vision promise?',
        'stone':'What will endure when the moment has passed?', 'city':'Who gets heard in this crowded world?',
        'laboratory':'What responsibility comes with the new power?', 'bed':'What can no longer be kept outside?',
    }
    for s in stories:
        base=s['scenes']
        for i,f in enumerate(base): f['previousIndex']=i;f['key']=f"{s['id']}:base:{i}"
        if not s.get('spoken'):
            assert s['id'] in EXTRA,s['id']
            additions=[]
            for j,line in enumerate(EXTRA[s['id']].splitlines()):
                after,title,text,motif=line.split('|');after=ANCHORS.get(s['id'],{}).get(title,int(after))
                # Match named cast in the text; otherwise keep the adjacent beat's cast.
                cast=[c['name'] for c in s['characters'] if c['name'].lower() in text.lower()]
                additions.append((after,dict(title=title,text=text,cast=cast or base[min(after-1,len(base)-1)]['cast'],motif=motif,cue=title.upper(),key=f"{s['id']}:extra:{j}",spoken=True)))
            out=[]
            for i,f in enumerate(base,1):
                # Preserve information, but address the listener and sharpen the spoken rhythm.
                text=f['text']
                text=text.replace('nevertheless','still').replace('subsequently','then').replace('nevertheless','still').replace('therefore','so')
                text=text.replace('cannot obtain','cannot find').replace('reveals','uncovers').replace('confronts','faces').replace('demonstrates','shows').replace('nevertheless','still')
                first,sep,rest=text.partition('. ')
                if sep and not first.endswith(('Mr','Mrs','Dr','St')):
                    text=first+'! '+rest
                lead=openings[(sum(map(ord,s['id']))+i-1)%len(openings)]
                # Questions invite interpretation rather than inventing dialogue or events.
                question=questions.get(f['motif'],'What will this moment change?')
                f['text']=lead+' '+text+' '+question
                f['spoken']=True
                out.append(f)
                out.extend(g for after,g in additions if after==i)
            s['scenes']=out
        assert len(s['scenes'])==12,(s['id'],len(s['scenes']))
        for i,f in enumerate(s['scenes']):
            f['chapter']=i+1
            f['mood']='sorrow' if f['motif']=='grave' else 'tension' if f['motif'] in ['chains','storm','ghost','sword','dagger','fire'] else 'wonder' if f['motif'] in ['stars','garden','bird','sunrise','music'] else 'resolve' if i==11 else 'curious'
        s['contentVersion']=3
